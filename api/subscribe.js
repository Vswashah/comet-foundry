const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

// Best-effort, single-instance rate limit. Vercel functions can scale to
// multiple warm instances, so this does not guarantee a hard global cap --
// but it does stop the common case (a script hammering the endpoint in a
// tight loop, which lands on the same warm instance) without needing an
// external store like Redis/Vercel KV. Revisit if abuse persists.
const WINDOW_MS = 60_000;
const MAX_PER_WINDOW = 5;
const hits = new Map(); // ip -> array of request timestamps

function isRateLimited(ip) {
  const now = Date.now();
  const timestamps = (hits.get(ip) || []).filter((t) => now - t < WINDOW_MS);
  timestamps.push(now);
  hits.set(ip, timestamps);

  // Bound memory: drop the oldest-tracked IP once the map gets large.
  if (hits.size > 5000) {
    hits.delete(hits.keys().next().value);
  }

  return timestamps.length > MAX_PER_WINDOW;
}

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ ok: false, error: 'Method not allowed' });
  }

  const ip = (req.headers['x-forwarded-for'] || req.socket?.remoteAddress || 'unknown').split(',')[0].trim();
  if (isRateLimited(ip)) {
    res.setHeader('Retry-After', '60');
    return res.status(429).json({ ok: false, error: 'Too many requests, try again in a minute' });
  }

  const { email, company } = req.body || {};

  // Honeypot: a real visitor never fills this hidden field, bots often do.
  if (company) {
    return res.status(200).json({ ok: true });
  }

  if (typeof email !== 'string' || !EMAIL_RE.test(email)) {
    return res.status(400).json({ ok: false, error: 'Invalid email address' });
  }

  try {
    const resendRes = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${process.env.RESEND_API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        from: 'Comet Foundry <subscribe@cometfoundry.com>',
        to: ['subscribe@cometfoundry.com'],
        reply_to: email,
        subject: 'New "Join The Foundry" signup',
        text: `New signup from the Join The Foundry form on cometfoundry.com:\n\nEmail: ${email}`
      })
    });

    if (!resendRes.ok) {
      const errBody = await resendRes.text();
      console.error('Resend API error:', resendRes.status, errBody);
      return res.status(502).json({ ok: false, error: 'Failed to send' });
    }

    return res.status(200).json({ ok: true });
  } catch (err) {
    console.error('Subscribe handler error:', err);
    return res.status(500).json({ ok: false, error: 'Server error' });
  }
}
