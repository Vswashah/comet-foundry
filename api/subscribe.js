const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ ok: false, error: 'Method not allowed' });
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
