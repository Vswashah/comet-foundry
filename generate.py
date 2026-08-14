import os

OUT = os.path.dirname(os.path.abspath(__file__))

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Comet Foundry</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=IBM+Plex+Mono:wght@400;500;700&family=Caveat:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body data-page="{page}">

  <div id="door">
    <div class="door-status mono" id="door-status"><span class="dot"></span>LAB STATUS: CLOSED</div>
    <h1 id="door-title">COMET<br>FOUNDRY</h1>
    <button id="open-btn">OPEN LAB →</button>
    <div id="door-meta" class="mono">EST. 2026 / UT DALLAS / LAB 01</div>
  </div>

  <main id="main">
    <header class="nav">
      <div class="wrap">
        <a class="brand-mark" href="index.html">COMET FOUNDRY</a>
        <nav class="nav-links">
          <a href="about.html" data-nav="about">About</a>
          <a href="programs.html" data-nav="programs">Programs</a>
          <a href="projects.html" data-nav="projects">Projects</a>
          <a href="team.html" data-nav="team">Team</a>
          <a href="partners.html" data-nav="partners">Partners</a>
          <a href="events.html" data-nav="events">Events</a>
          <a href="blog.html" data-nav="blog">Blog</a>
        </nav>
        <a class="nav-cta" href="https://forms.cloud.microsoft/pages/responsepage.aspx?id=HR0ojU2c90uxbgMtFd6fbIhHjy7i2rpHt7VcaeT3yedUMkQwTTU4TkpUNFczMVQzS0cwUUVaWEw0WC4u&route=shorturl&b2b=true" target="_blank" rel="noopener">APPLY →</a>
        <button id="nav-toggle" class="nav-toggle" aria-label="Toggle menu" aria-expanded="false">☰</button>
      </div>
      <div id="mobile-menu" class="mobile-menu">
        <a href="about.html" data-nav="about">About</a>
        <a href="programs.html" data-nav="programs">Programs</a>
        <a href="projects.html" data-nav="projects">Projects</a>
        <a href="team.html" data-nav="team">Team</a>
        <a href="partners.html" data-nav="partners">Partners</a>
        <a href="events.html" data-nav="events">Events</a>
        <a href="blog.html" data-nav="blog">Blog</a>
        <a href="https://forms.cloud.microsoft/pages/responsepage.aspx?id=HR0ojU2c90uxbgMtFd6fbIhHjy7i2rpHt7VcaeT3yedUMkQwTTU4TkpUNFczMVQzS0cwUUVaWEw0WC4u&route=shorturl&b2b=true" target="_blank" rel="noopener" class="cta-row">Apply →</a>
      </div>
    </header>
"""

FOOTER = """
    <footer>
      <div class="wrap">
        <div class="footer-top">
          <div class="footer-brand">
            <h4>Comet Foundry</h4>
            <p>A hacker house at UTD. No perfect ideas. Just interesting ones.</p>
          </div>
          <div class="footer-links">
            <div>
              <h5>Explore</h5>
              <ul>
                <li><a href="about.html">About</a></li>
                <li><a href="programs.html">Programs</a></li>
                <li><a href="projects.html">Projects</a></li>
                <li><a href="team.html">Team</a></li>
                <li><a href="partners.html">Partners</a></li>
                <li><a href="events.html">Events</a></li>
                <li><a href="blog.html">Blog</a></li>
              </ul>
            </div>
            <div>
              <h5>Contact</h5>
              <ul>
                <li><a href="mailto:info@cometfoundry.com">info@cometfoundry.com</a></li>
                <li><a href="https://forms.cloud.microsoft/pages/responsepage.aspx?id=HR0ojU2c90uxbgMtFd6fbIhHjy7i2rpHt7VcaeT3yedUMkQwTTU4TkpUNFczMVQzS0cwUUVaWEw0WC4u&route=shorturl&b2b=true" target="_blank" rel="noopener">Apply →</a></li>
              </ul>
              <div class="social-icons">
                <a href="https://www.linkedin.com/company/cometfoundry/" target="_blank" rel="noopener" aria-label="Comet Foundry on LinkedIn">
                  <svg viewBox="0 0 24 24"><path d="M4.98 3.5C4.98 4.88 3.87 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1s2.48 1.12 2.48 2.5zM.5 8h4v15h-4V8zm7.5 0h3.8v2.05h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1V23h-4v-6.9c0-1.65-.03-3.77-2.3-3.77-2.3 0-2.65 1.8-2.65 3.65V23h-4V8z"/></svg>
                </a>
                <a href="https://www.instagram.com/cometfoundry" target="_blank" rel="noopener" aria-label="Comet Foundry on Instagram">
                  <svg viewBox="0 0 24 24"><path d="M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41-.56-.22-.96-.48-1.38-.9-.42-.42-.68-.82-.9-1.38-.16-.42-.36-1.06-.41-2.23C2.17 15.58 2.16 15.2 2.16 12s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.42 2.17 8.8 2.16 12 2.16M12 0C8.74 0 8.33.01 7.05.07 5.78.13 4.9.33 4.14.63c-.79.31-1.46.72-2.13 1.38C1.35 2.68.94 3.35.63 4.14.33 4.9.13 5.78.07 7.05.01 8.33 0 8.74 0 12s.01 3.67.07 4.95c.06 1.27.26 2.15.56 2.91.31.79.72 1.46 1.38 2.13.67.66 1.34 1.07 2.13 1.38.76.3 1.64.5 2.91.56C8.33 23.99 8.74 24 12 24s3.67-.01 4.95-.07c1.27-.06 2.15-.26 2.91-.56.79-.31 1.46-.72 2.13-1.38.66-.67 1.07-1.34 1.38-2.13.3-.76.5-1.64.56-2.91.06-1.28.07-1.69.07-4.95s-.01-3.67-.07-4.95c-.06-1.27-.26-2.15-.56-2.91-.31-.79-.72-1.46-1.38-2.13C20.32 1.35 19.65.94 18.86.63c-.76-.3-1.64-.5-2.91-.56C14.67.01 14.26 0 12 0zm0 5.84A6.16 6.16 0 1 0 18.16 12 6.16 6.16 0 0 0 12 5.84zM12 16a4 4 0 1 1 4-4 4 4 0 0 1-4 4zm6.41-10.87a1.44 1.44 0 1 1-1.44-1.44 1.44 1.44 0 0 1 1.44 1.44z"/></svg>
                </a>
                <a href="https://discord.com/invite/Hdg8VBFUW" target="_blank" rel="noopener" aria-label="Comet Foundry on Discord">
                  <svg viewBox="0 0 24 24"><path d="M20.317 4.37a19.79 19.79 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.056 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994a.076.076 0 0 0-.041-.106 13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128c.126-.094.252-.192.372-.291a.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 0 1 .078.01c.12.099.246.198.373.292a.077.077 0 0 1-.006.127 12.3 12.3 0 0 1-1.873.892.076.076 0 0 0-.04.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.055c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.331c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.418 2.157-2.418 1.21 0 2.176 1.094 2.157 2.418 0 1.334-.955 2.419-2.157 2.419zm7.974 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.418 2.157-2.418 1.21 0 2.176 1.094 2.157 2.418 0 1.334-.946 2.419-2.157 2.419z"/></svg>
                </a>
              </div>
            </div>
            <div>
              <h5>Legal</h5>
              <ul>
                <li><a href="privacy-policy.html">Privacy Policy</a></li>
                <li><a href="terms-of-use.html">Terms of Use</a></li>
              </ul>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <span class="mono">© 2026 Comet Foundry. All rights reserved.</span>
          <span class="footer-easter">Built by humans — every em dash placed manually. :)</span>
          <span class="mono fb-right">EST. 2026 / UT DALLAS</span>
        </div>
      </div>
    </footer>
  </main>

  <button id="bored-btn">I'M BORED →</button>
  <div id="bored-popup">
    <div class="result" id="bored-result">Build something.</div>
    <span>tap again for another one</span>
  </div>

  <script src="script.js"></script>
</body>
</html>
"""

def write(fname, title, page, body):
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(HEAD.format(title=title, page=page))
        f.write(body)
        f.write(FOOTER)

# ---------------- HOME ----------------
home_body = """
    <section class="hero">
      <div class="wrap">
        <div class="eyebrow"><span class="dot"></span>LAB STATUS: OPEN</div>
        <h1 class="mega"><span>NOT A CLUB</span><span class="orange">A FOUNDRY</span></h1>
        <div class="hero-note hand">a hacker house at UTD :)</div>
        <p class="hero-sub">A hacker house for people who'd rather build the weird thing than plan the safe one. Yes, this is technically a student org. We're figuring it out too.</p>
        <div class="hero-tags">
          <span class="tag">NO PERFECT IDEAS. JUST INTERESTING ONES.</span>
          <span class="tag">MADE AT UTD</span>
        </div>
      </div>
    </section>

    <div class="strip">
      <div class="strip-track mono">
        <span>IDEA → 01</span><span>TEST → 02</span><span>BUILD → 03</span><span>SHIP → 04</span><span>REPEAT → ∞</span>
        <span>IDEA → 01</span><span>TEST → 02</span><span>BUILD → 03</span><span>SHIP → 04</span><span>REPEAT → ∞</span>
        <span>IDEA → 01</span><span>TEST → 02</span><span>BUILD → 03</span><span>SHIP → 04</span><span>REPEAT → ∞</span>
        <span>IDEA → 01</span><span>TEST → 02</span><span>BUILD → 03</span><span>SHIP → 04</span><span>REPEAT → ∞</span>
        <span>IDEA → 01</span><span>TEST → 02</span><span>BUILD → 03</span><span>SHIP → 04</span><span>REPEAT → ∞</span>
        <span>IDEA → 01</span><span>TEST → 02</span><span>BUILD → 03</span><span>SHIP → 04</span><span>REPEAT → ∞</span>
        <span>IDEA → 01</span><span>TEST → 02</span><span>BUILD → 03</span><span>SHIP → 04</span><span>REPEAT → ∞</span>
        <span>IDEA → 01</span><span>TEST → 02</span><span>BUILD → 03</span><span>SHIP → 04</span><span>REPEAT → ∞</span>
      </div>
    </div>

    <section class="tight">
      <div class="wrap">
        <div class="sec-head">
          <span class="num">EXP 000 / WHAT WE ARE</span>
          <h2>The Lab, in one paragraph</h2>
        </div>
        <div class="about-grid">
          <div class="about-text">
            <p>Comet Foundry is a space at UTD for building things nobody assigned you.</p>
            <p>No club meetings that go nowhere, no "great idea, let's revisit next semester." Just a room, some people who ship, and a running list of experiments in progress.</p>
            <a class="lab-link mono" href="about.html" style="border-bottom:1px solid var(--flask); color:var(--flask); text-decoration:none; font-size:13px;">Read the full story →</a>
          </div>
          <div class="doc-card">
            <span class="hand">currently cooking</span>
            <h3>Active Experiments</h3>
            <ul class="mono">
              <li><span>Peer matching for team formation</span><span class="v">TESTING</span></li>
              <li><span>Micro-grants for weekend builds</span><span class="v">LIVE</span></li>
              <li><span>Open critique nights</span><span class="v">NO RESULTS YET</span></li>
              <li><span>Alumni founder network</span><span class="v">IDEA → 01</span></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="tight">
      <div class="wrap">
        <div class="sec-head">
          <span class="num">EXP 001 / HOW WE HELP</span>
          <h2>Four Labs</h2>
          <p>Not departments. Just the four things worth doing here, sorted by what you're actually in the mood for.</p>
        </div>
        <div class="labs-grid">
          <div class="lab-card">
            <span class="lab-annot hand">seriously, anything</span>
            <div>
              <span class="code mono">LAB / 01</span>
              <h3>Build Lab</h3>
              <p class="cmd mono">Make things.</p>
            </div>
            <div class="lab-actions">
              <a class="lab-link" href="programs.html">See what's on →</a>
              <span class="stamp">MAKE →</span>
            </div>
          </div>
          <div class="lab-card">
            <div>
              <span class="code mono">LAB / 02</span>
              <h3>Think Lab</h3>
              <p class="cmd mono">Have an opinion.</p>
            </div>
            <div class="lab-actions">
              <a class="lab-link" href="programs.html">See what's on →</a>
              <span class="stamp">preferably controversial</span>
            </div>
          </div>
          <div class="lab-card">
            <div>
              <span class="code mono">LAB / 03</span>
              <h3>Network Lab</h3>
              <p class="cmd mono">Meet people.</p>
            </div>
            <div class="lab-actions">
              <a class="lab-link" href="programs.html">See what's on →</a>
              <span class="stamp">the useful kind</span>
            </div>
          </div>
          <div class="lab-card">
            <div>
              <span class="code mono">LAB / 04</span>
              <h3>After Hours</h3>
              <p class="cmd mono">Touch grass. 😂</p>
            </div>
            <div class="lab-actions">
              <a class="lab-link" href="programs.html">See what's on →</a>
              <span class="stamp">occasionally</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ================= DEMO DAY ================= -->
    <section class="demoday" id="demo-day">
      <div class="demoday-pin wrap">
        <p class="demoday-meta">COMET FOUNDRY / FALL 2026 / FINAL EXPERIMENT</p>

        <div class="demoday-title" id="demoday-title">
          <span class="word">DEMO</span>
          <span class="word day">DAY</span>
        </div>

        <p class="demoday-subhead">Show Us What You Made.</p>

        <div class="demoday-meta-row">
          <span class="demoday-pill">DECEMBER 2026</span>
          <span class="demoday-pill status">STATUS: IN PROGRESS</span>
        </div>

        <p class="demoday-sub">All semester, Comet Foundry is building, questioning, connecting, and experimenting. Demo Day is where it all comes together.</p>
        <p class="demoday-sub2">You don't need a startup. You don't need a perfect product. You just need something you made.</p>

        <div class="demoday-cta">
          <div class="demoday-cta-buttons">
            <a class="demoday-btn-primary" href="https://forms.cloud.microsoft/pages/responsepage.aspx?id=HR0ojU2c90uxbgMtFd6fbIhHjy7i2rpHt7VcaeT3yedUMkQwTTU4TkpUNFczMVQzS0cwUUVaWEw0WC4u&route=shorturl&b2b=true" target="_blank" rel="noopener">BUILD TOWARD DEMO DAY →</a>
          </div>
          <span class="demoday-hand hand">someone had to try. :)</span>
        </div>
      </div>
    </section>

    <section class="tight">
      <div class="wrap">
        <div class="sec-head">
          <span class="num">EXP 002 / WHO'S IN THE ROOM</span>
          <h2>Partner Spotlight</h2>
        </div>
        <div class="partner-card" style="max-width:640px;">
          <div class="card-media">
            <span class="tagpill mono">FEATURED PARTNER</span>
          </div>
          <div class="card-body">
            <h3>RESILIENT PRIVACY Inc.</h3>
            <p>Comet Foundry's founding Industry Partner — advisory only, non-voting. Coordinates mentorship and internship referrals for opted-in members.</p>
            <a class="card-link" href="partners.html">See all partners →</a>
          </div>
        </div>
      </div>
    </section>

    <section class="tight">
      <div class="wrap">
        <div class="sec-head">
          <span class="num">EXP 003 / WHAT'S HAPPENING</span>
          <h2>Next Up</h2>
        </div>
        <div class="event-card">
          <span class="event-annot hand">you should probably come to this</span>
          <div class="event-left">
            <div class="event-date">SEP 01 / 7:00 PM</div>
            <h3>Foundry Kickoff Night</h3>
            <p>First open house of the semester. Tour the space, pitch a half-formed idea, find someone to build it with.</p>
          </div>
          <div class="event-right">
            <div class="row"><span>STATUS</span><b>EXPERIMENT IN PROGRESS</b></div>
            <div class="row"><span>LOCATION</span><b>UT Dallas — Lab 01</b></div>
            <a class="rsvp-btn" href="event-kickoff-night.html">RSVP →</a>
          </div>
        </div>
        <div style="text-align:right; margin-top:24px;">
          <a class="lab-link mono" href="events.html" style="color:var(--ink-soft); border-bottom:1px solid var(--line); text-decoration:none; font-size:13px;">See all events →</a>
        </div>
      </div>
    </section>

    <section class="join">
      <div class="wrap">
        <div class="sec-head center">
          <span class="num mono">EXP 004 / GET IN</span>
          <h2>Join The Foundry</h2>
          <p>One email. We'll tell you when the door's open.</p>
        </div>
        <form class="join-form" onsubmit="event.preventDefault(); this.querySelector('button').textContent='ADDED ✓';">
          <input type="email" placeholder="you@utdallas.edu" required aria-label="Email address">
          <button type="submit">JOIN FOUNDRY →</button>
        </form>
        <div class="join-note">NO SPAM. NO PERFECT IDEAS. JUST INTERESTING ONES. &nbsp;·&nbsp; <a href="https://forms.cloud.microsoft/pages/responsepage.aspx?id=HR0ojU2c90uxbgMtFd6fbIhHjy7i2rpHt7VcaeT3yedUMkQwTTU4TkpUNFczMVQzS0cwUUVaWEw0WC4u&route=shorturl&b2b=true" target="_blank" rel="noopener" style="color:var(--ink-soft);">Full application →</a></div>
      </div>
    </section>
"""
write("index.html", "Home", "home", home_body)

# ---------------- ABOUT ----------------
about_body = """
    <section class="page-hero">
      <div class="wrap">
        <div class="breadcrumb"><a href="index.html">Home</a> / About</div>
        <h1>The Story</h1>
        <span class="hero-note hand">why a hacker house?</span>
        <p class="lede">Comet Foundry started because the good ideas at UTD kept dying in group chats instead of becoming things.</p>
      </div>
    </section>

    <section class="tight">
      <div class="wrap about-grid">
        <div class="about-text">
          <p>We're a small group of students who got tired of waiting for permission to build. So we started a room.</p>
          <p>No advisor sign-off required to try something. No semester-long approval process. If you want to build it, test it, or argue about it, there's a lab for that — starting this week, not next year.</p>
          <p>Comet Foundry isn't a résumé line. It's a space that assumes you're capable of more than a class project, and gets out of your way.</p>
        </div>
        <div class="doc-card">
          <span class="hand">the short version</span>
          <h3>Why A Hacker House</h3>
          <ul class="mono">
            <li><span>Space that's open late</span><span class="v">YES</span></li>
            <li><span>People who'll actually build with you</span><span class="v">YES</span></li>
            <li><span>Gatekeeping by GPA or résumé</span><span class="v">NO</span></li>
            <li><span>Meetings that could've been an email</span><span class="v">NO</span></li>
          </ul>
        </div>
      </div>
    </section>

    <section class="tight">
      <div class="wrap">
        <div class="sec-head">
          <span class="num">VALUES</span>
          <h2>What We Actually Believe</h2>
        </div>
        <div class="values-grid">
          <div class="value-card">
            <span class="code mono">01</span>
            <div>
              <h3>Every Background Welcome</h3>
              <p>CS major, art major, undeclared — if you want to build, there's a seat.</p>
            </div>
          </div>
          <div class="value-card">
            <span class="code mono">02</span>
            <div>
              <h3>Ideas Over Résumés</h3>
              <p>We care what you want to make, not what's already on your LinkedIn.</p>
            </div>
          </div>
          <div class="value-card">
            <span class="code mono">03</span>
            <div>
              <h3>Bias Toward Shipping</h3>
              <p>A rough thing that exists beats a perfect thing that doesn't.</p>
            </div>
          </div>
          <div class="value-card">
            <span class="code mono">04</span>
            <div>
              <h3>Community Over Competition</h3>
              <p>We'd rather you find a co-founder here than a rival.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="join">
      <div class="wrap">
        <div class="sec-head center">
          <span class="num mono">READY?</span>
          <h2>Come Build With Us</h2>
        </div>
        <a class="rsvp-btn" href="https://forms.cloud.microsoft/pages/responsepage.aspx?id=HR0ojU2c90uxbgMtFd6fbIhHjy7i2rpHt7VcaeT3yedUMkQwTTU4TkpUNFczMVQzS0cwUUVaWEw0WC4u&route=shorturl&b2b=true" target="_blank" rel="noopener" style="background:var(--ink); color:var(--paper);">APPLY TO JOIN →</a>
      </div>
    </section>
"""
write("about.html", "About", "about", about_body)

# ---------------- PROGRAMS ----------------
programs_body = """
    <section class="page-hero">
      <div class="wrap">
        <div class="breadcrumb"><a href="index.html">Home</a> / Programs</div>
        <h1>Four Labs</h1>
        <span class="hero-note hand">pick your mood</span>
        <p class="lede">Not departments — just the four things worth doing here. Drop into whichever matches what you're in the mood for this week.</p>
      </div>
    </section>

    <section class="tight">
      <div class="wrap">
        <div class="labs-grid">
          <div class="lab-card" style="min-height:340px;">
            <span class="lab-annot hand">seriously, anything</span>
            <div>
              <span class="code mono">LAB / 01</span>
              <h3>Build Lab</h3>
              <p class="cmd mono">Make things.</p>
              <p class="detail">Weekend build sprints, prototyping sessions, and open workshop hours with the hardware bench and dev tools. Show up with an idea, leave with a v1.</p>
            </div>
            <div class="lab-actions">
              <a class="lab-link" href="events.html">See Build Lab events →</a>
              <span class="stamp">MAKE →</span>
            </div>
          </div>
          <div class="lab-card" style="min-height:340px;">
            <div>
              <span class="code mono">LAB / 02</span>
              <h3>Think Lab</h3>
              <p class="cmd mono">Have an opinion.</p>
              <p class="detail">Mentorship, research discussions, and 1:1 feedback sessions. Bring a half-formed argument and leave with a sharper one — preferably a controversial one.</p>
            </div>
            <div class="lab-actions">
              <a class="lab-link" href="events.html">See Think Lab events →</a>
              <span class="stamp">preferably controversial</span>
            </div>
          </div>
          <div class="lab-card" style="min-height:340px;">
            <div>
              <span class="code mono">LAB / 03</span>
              <h3>Network Lab</h3>
              <p class="cmd mono">Meet people.</p>
              <p class="detail">Demo nights, founder dinners, and industry partnerships. The useful kind of networking — the kind where you actually stay in touch.</p>
            </div>
            <div class="lab-actions">
              <a class="lab-link" href="events.html">See Network Lab events →</a>
              <span class="stamp">the useful kind</span>
            </div>
          </div>
          <div class="lab-card" style="min-height:340px;">
            <div>
              <span class="code mono">LAB / 04</span>
              <h3>After Hours</h3>
              <p class="cmd mono">Touch grass. 😂</p>
              <p class="detail">Informal hangouts, game nights, and the community that makes the other three labs worth showing up for. Occasionally, we go outside.</p>
            </div>
            <div class="lab-actions">
              <a class="lab-link" href="events.html">See After Hours events →</a>
              <span class="stamp">occasionally</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="join">
      <div class="wrap">
        <div class="sec-head center">
          <span class="num mono">NEXT STEP</span>
          <h2>Find Your Lab</h2>
          <p>Check what's actually on the calendar this month.</p>
        </div>
        <a class="rsvp-btn" href="events.html" style="background:var(--ink); color:var(--paper);">VIEW EVENTS →</a>
      </div>
    </section>
"""
write("programs.html", "Programs", "programs", programs_body)

# ---------------- PROJECTS ----------------
def coming_soon_card():
    return """
          <div class="coming-soon-card">
            <span class="tag mono">COMING SOON</span>
            <h3>Member Project</h3>
            <p>This spot's open. Member-built projects will show up here as they ship.</p>
          </div>"""

projects_body = """
    <section class="page-hero">
      <div class="wrap">
        <div class="breadcrumb"><a href="index.html">Home</a> / Projects</div>
        <h1>Built Here</h1>
        <span class="hero-note hand">no results yet, some of the time</span>
        <p class="lede">This wall is just getting started — nothing shipped yet, but this is where it'll live once it does.</p>
      </div>
    </section>

    <section class="tight">
      <div class="wrap">
        <div class="card-grid">""" + \
    coming_soon_card() + \
    coming_soon_card() + \
    coming_soon_card() + """
        </div>
      </div>
    </section>

    <section class="join">
      <div class="wrap">
        <div class="sec-head center">
          <span class="num mono">YOUR TURN</span>
          <h2>Add Yours To The Wall</h2>
        </div>
        <a class="rsvp-btn" href="https://forms.cloud.microsoft/pages/responsepage.aspx?id=HR0ojU2c90uxbgMtFd6fbIhHjy7i2rpHt7VcaeT3yedUMkQwTTU4TkpUNFczMVQzS0cwUUVaWEw0WC4u&route=shorturl&b2b=true" target="_blank" rel="noopener" style="background:var(--ink); color:var(--paper);">START BUILDING →</a>
      </div>
    </section>
"""
write("projects.html", "Projects", "projects", projects_body)

# ---------------- TEAM ----------------
def person_card(lead, role, email_slug, seat_label=None):
    subtitle = f"{role} — {seat_label}" if seat_label else role
    abbr = "".join(w[0] for w in role.split()).upper()
    photo_cls = "profile-photo lead" if lead else "profile-photo"
    return f"""
          <div class="profile-card">
            <div class="{photo_cls}">
              <span class="profile-tag">OPEN POSITION</span>
              <span class="abbr">{abbr}</span>
            </div>
            <div class="profile-body">
              <h3>Name TBD</h3>
              <div class="profile-role">{subtitle}</div>
              <div class="profile-links">
                <a href="mailto:{email_slug}@cometfoundry.com">{email_slug}@cometfoundry.com</a>
                <a href="javascript:void(0)" class="linkedin-placeholder">Add LinkedIn →</a>
              </div>
            </div>
          </div>"""

EXEC_BOARD = [
    ("President", "president"),
    ("Vice President", "vp"),
    ("Secretary", "secretary"),
    ("Treasurer", "treasurer"),
    ("Marketing Strategist", "marketing"),
]

OFFICERS = [
    ("Innovation Officer", "innovation", 1),
    ("Technology Officer", "tech", 1),
    ("Events Officer", "events", 3),
    ("Public Relations Officer", "pr", 1),
    ("Partnerships Officer", "partnerships", 2),
    ("Community Engagement Officer", "community", 1),
    ("Social Media Officer", "social", 2),
    ("Design Officer", "design", 1),
    ("Outreach Officer", "outreach", 1),
]

exec_cards = "".join(person_card(True, role, slug) for role, slug in EXEC_BOARD)

officer_cards = ""
for role, slug, seats in OFFICERS:
    if seats == 1:
        officer_cards += person_card(False, role, slug)
    else:
        for i in range(1, seats + 1):
            officer_cards += person_card(False, role, f"{slug}{i}", seat_label=f"Seat {i} of {seats}")

team_body = """
    <section class="page-hero">
      <div class="wrap">
        <div class="breadcrumb"><a href="index.html">Home</a> / Team</div>
        <h1>Who Runs This</h1>
        <span class="hero-note hand">mostly figuring it out live</span>
        <p class="lede">Our org chart — Executive Board and Officer seats. Most are still open. If one fits you, apply below.</p>
      </div>
    </section>

    <section class="tight">
      <div class="wrap">
        <span class="section-label">EXECUTIVE BOARD</span>
        <div class="profile-grid">""" + exec_cards + """
        </div>
      </div>
    </section>

    <section class="tight">
      <div class="wrap">
        <span class="section-label">OFFICERS</span>
        <div class="profile-grid">""" + officer_cards + """
        </div>
      </div>
    </section>

    <section class="join">
      <div class="wrap">
        <div class="sec-head center">
          <span class="num mono">JOIN THEM</span>
          <h2>Be On This Page Next</h2>
        </div>
        <a class="rsvp-btn" href="https://forms.cloud.microsoft/pages/responsepage.aspx?id=HR0ojU2c90uxbgMtFd6fbIhHjy7i2rpHt7VcaeT3yedUQVE2MU1DUE80TkpGTEpURDhUUFBXQUo0MS4u&route=shorturl" target="_blank" rel="noopener" style="background:var(--ink); color:var(--paper);">APPLY →</a>
      </div>
    </section>
"""
write("team.html", "Team", "team", team_body)


# ---------------- PARTNERS ----------------
def partner_card(grad, name, blurb, url=None):
    link_html = f'<a class="card-link" href="{url}" target="_blank" rel="noopener">Visit site →</a>' if url else ""
    return f"""
          <div class="partner-card">
            <div class="card-media {grad}"></div>
            <div class="card-body">
              <h3>{name}</h3>
              <p>{blurb}</p>
              {link_html}
            </div>
          </div>"""

def coming_soon_partner_card():
    return """
          <div class="coming-soon-card">
            <span class="tag mono">COMING SOON</span>
            <h3>Partner</h3>
            <p>This spot's open. New industry partners will show up here as they join.</p>
          </div>"""

partners_body = """
    <section class="page-hero">
      <div class="wrap">
        <div class="breadcrumb"><a href="index.html">Home</a> / Partners</div>
        <h1>Who Backs The Lab</h1>
        <span class="hero-note hand">the useful kind, again</span>
        <p class="lede">Industry partners who fund experiments, send mentors, and show up for demo nights.</p>
      </div>
    </section>

    <section class="tight">
      <div class="wrap">
        <div class="card-grid">""" + \
    partner_card("", "RESILIENT PRIVACY Inc.", "Comet Foundry's founding Industry Partner — advisory only, non-voting. Coordinates mentorship and internship referrals for opted-in members.", "https://www.resilientprivacy.com") + \
    coming_soon_partner_card() + \
    coming_soon_partner_card() + """
        </div>
      </div>
    </section>

    <section class="join">
      <div class="wrap">
        <div class="sec-head center">
          <span class="num mono">FOR COMPANIES</span>
          <h2>Become A Partner</h2>
          <p>Fund an experiment, send a mentor, or just come to a demo night and see what's brewing.</p>
        </div>
        <a class="rsvp-btn" href="mailto:partners@cometfoundry.com" style="background:var(--ink); color:var(--paper);">GET IN TOUCH →</a>
      </div>
    </section>
"""
write("partners.html", "Partners", "partners", partners_body)

# ---------------- EVENTS ----------------
def event_row(date, title, blurb, href):
    return f"""
        <a class="event-list-row" href="{href}">
          <span class="elr-date mono">{date}</span>
          <div>
            <h4>{title}</h4>
            <p>{blurb}</p>
          </div>
          <span class="elr-arrow">VIEW →</span>
        </a>"""

events_body = """
    <section class="page-hero">
      <div class="wrap">
        <div class="breadcrumb"><a href="index.html">Home</a> / Events</div>
        <h1>What's Happening</h1>
        <span class="hero-note hand">you should probably come to this</span>
        <p class="lede">Build sprints, critique nights, demo nights, and the occasional excuse to touch grass.</p>
      </div>
    </section>

    <section class="tight">
      <div class="wrap">
        <div class="cal-card">
          <div class="cal-toolbar">
            <button class="cal-btn" id="cal-today">Today</button>
            <div class="cal-nav">
              <button class="cal-arrow" id="cal-prev" aria-label="Previous month">←</button>
              <button class="cal-arrow" id="cal-next" aria-label="Next month">→</button>
            </div>
            <span class="cal-month-label" id="cal-month-label">August 2026</span>
            <span class="cal-view">Month</span>
          </div>
          <div class="cal-grid" id="cal-grid"></div>
          <div class="cal-footer">
            <div class="who">
              <b>info@cometfoundry.com</b>
              <div class="tz">Events shown in time zone: (GMT-05:00) Central Time — Chicago</div>
              <a class="outlook-link" id="cal-outlook-link" href="#" target="_blank" rel="noopener">Add to Outlook Calendar →</a>
            </div>
            <div class="cal-provider"><span class="sq"><span></span><span></span><span></span><span></span></span> Microsoft Outlook</div>
          </div>
        </div>

        <div class="cal-cta-wrap">
          <button class="cal-cta" id="add-cal-btn">ADD IT TO YOUR CALENDAR &lt;3</button>
          <div class="cal-cta-note">Downloads Kickoff Night as a .ics — works with Outlook, Google, and Apple Calendar.</div>
        </div>
      </div>
    </section>

    <section class="tight">
      <div class="wrap">
        <div class="event-card">
          <span class="event-annot hand">next up</span>
          <div class="event-left">
            <div class="event-date">SEP 01 / 7:00 PM</div>
            <h3>Foundry Kickoff Night</h3>
            <p>First open house of the semester. Tour the space, pitch a half-formed idea, find someone to build it with.</p>
          </div>
          <div class="event-right">
            <div class="row"><span>STATUS</span><b>EXPERIMENT IN PROGRESS</b></div>
            <div class="row"><span>LOCATION</span><b>UT Dallas — Lab 01</b></div>
            <a class="rsvp-btn" href="event-kickoff-night.html">RSVP →</a>
          </div>
        </div>

        <div class="sec-head" style="margin-top:60px; margin-bottom:0;">
          <span class="num">UPCOMING</span>
          <h2 style="font-size:clamp(24px,4vw,32px);">More On The Calendar</h2>
        </div>
        <div class="coming-soon-card" style="margin-top:24px;">
          <span class="tag mono">COMING SOON</span>
          <h3>Event</h3>
          <p>Nothing else on the calendar yet — check back as the semester fills in.</p>
        </div>
      </div>
    </section>
"""
write("events.html", "Events", "events", events_body)

# ---------------- EVENT DETAIL ----------------
event_detail_body = """
    <section class="page-hero">
      <div class="wrap">
        <div class="breadcrumb"><a href="index.html">Home</a> / <a href="events.html">Events</a> / Kickoff Night</div>
        <h1>Foundry Kickoff Night</h1>
        <span class="hero-note hand">you should probably come to this</span>
      </div>
    </section>

    <section class="tight">
      <div class="wrap about-grid">
        <div class="about-text">
          <p>First open house of the semester. Tour the space, pitch a half-formed idea out loud, and find someone to build it with. No pitch deck required — a napkin sketch is plenty.</p>
          <p>Expect a short intro to the four labs, free food, and enough people in the room that you'll leave with at least one new collaborator.</p>
        </div>
        <div class="doc-card">
          <span class="hand">the details</span>
          <h3>Event Info</h3>
          <ul class="mono">
            <li><span>Date</span><span class="v">SEP 01, 2026</span></li>
            <li><span>Time</span><span class="v">7:00 PM</span></li>
            <li><span>Location</span><span class="v">UT Dallas — Lab 01</span></li>
            <li><span>Status</span><span class="v">EXPERIMENT IN PROGRESS</span></li>
          </ul>
        </div>
      </div>
    </section>

    <section class="join">
      <div class="wrap">
        <div class="sec-head center">
          <span class="num mono">SAVE YOUR SPOT</span>
          <h2>RSVP</h2>
        </div>
        <a class="rsvp-btn" href="apply.html" style="background:var(--ink); color:var(--paper);">RSVP →</a>
      </div>
    </section>
"""
write("event-kickoff-night.html", "Kickoff Night", "events", event_detail_body)

# ---------------- BLOG ----------------
def post_card(grad, date, title, excerpt, href):
    return f"""
          <div class="post-card">
            <div class="card-media {grad}"></div>
            <div class="card-body">
              <span class="mono-small">{date}</span>
              <h3>{title}</h3>
              <p>{excerpt}</p>
              <a class="card-link" href="{href}">Read →</a>
            </div>
          </div>"""

def coming_soon_post_card():
    return """
          <div class="coming-soon-card">
            <span class="tag mono">COMING SOON</span>
            <h3>Post</h3>
            <p>This spot's open. Notes and updates from the lab will show up here as they're written.</p>
          </div>"""

blog_body = """
    <section class="page-hero">
      <div class="wrap">
        <div class="breadcrumb"><a href="index.html">Home</a> / Blog</div>
        <h1>Notes From The Lab</h1>
        <span class="hero-note hand">under construction lol</span>
        <p class="lede">Updates, postmortems, and the occasional controversial opinion from Think Lab.</p>
      </div>
    </section>

    <section class="tight">
      <div class="wrap">
        <div class="card-grid">""" + \
    coming_soon_post_card() + \
    coming_soon_post_card() + \
    coming_soon_post_card() + """
        </div>
      </div>
    </section>
"""
write("blog.html", "Blog", "blog", blog_body)

# ---------------- APPLY ----------------
apply_body = """
    <section class="page-hero">
      <div class="wrap">
        <div class="breadcrumb"><a href="index.html">Home</a> / Apply</div>
        <h1>Apply</h1>
        <span class="hero-note hand">ideas over résumés</span>
        <p class="lede">Tell us what you want to build. That's most of the application.</p>
      </div>
    </section>

    <section class="tight">
      <div class="wrap">
        <form class="apply-form" onsubmit="event.preventDefault(); this.querySelector('button').textContent='SUBMITTED ✓';">
          <div>
            <label for="name">Name</label>
            <input type="text" id="name" required>
          </div>
          <div>
            <label for="email">Email</label>
            <input type="email" id="email" required>
          </div>
          <div>
            <label for="year">Major / Year</label>
            <input type="text" id="year" placeholder="e.g. CS, Sophomore">
          </div>
          <div>
            <label for="build">What do you want to build?</label>
            <textarea id="build" placeholder="A rough idea is plenty."></textarea>
          </div>
          <div>
            <label for="heard">How'd you hear about us?</label>
            <select id="heard">
              <option>A friend</option>
              <option>An event</option>
              <option>Social media</option>
              <option>Other</option>
            </select>
          </div>
          <button type="submit">SUBMIT APPLICATION →</button>
          <span class="apply-note">We read every application ourselves. No perfect ideas required.</span>
        </form>
      </div>
    </section>
"""
write("apply.html", "Apply", "apply", apply_body)

# ---------------- LEGAL (Privacy Policy / Terms of Use) ----------------
def legal_shell(title, effective, body_html):
    return f"""
    <section class="page-hero">
      <div class="wrap">
        <div class="breadcrumb"><a href="index.html">Home</a> / {title}</div>
        <h1>{title}</h1>
      </div>
    </section>

    <section class="tight">
      <div class="wrap">
        <div class="legal-body">
          <div class="legal-effective">{effective}</div>
{body_html}
        </div>
      </div>
    </section>
"""

privacy_policy_body = legal_shell("Privacy Policy", "EFFECTIVE DATE: AUGUST 1, 2026 &nbsp;|&nbsp; LAST UPDATED: AUGUST 1, 2026", """
          <h2>1. Introduction</h2>
          <p>Comet Foundry ("Comet Foundry," "we," "us," or "our") is a student-led innovation, entrepreneurship, and technology organization registered as a student organization at the University of Texas at Dallas ("UT Dallas") through its Student Organization Center ("SOC"). This Privacy Policy ("Policy") describes how we collect, use, disclose, retain, and protect information in connection with cometfoundry.com (the "Site") and our related programs and communications (collectively, the "Services").</p>
          <p>By accessing or using the Services, you acknowledge that you have read and understood this Policy. If you do not agree with any part of this Policy, you should discontinue use of the Services.</p>

          <h2>2. No Independent Verification of Student Status</h2>
          <p>Comet Foundry does not request, receive, or verify a member's enrollment status, academic records, or other education records from UT Dallas or the SOC. Eligibility for officer or voting membership roles is confirmed solely through self-attestation by the individual, consistent with the Family Educational Rights and Privacy Act (FERPA), which prohibits Comet Foundry from accessing such records without the student's direct, independent authorization.</p>

          <h2>3. Information We Collect</h2>
          <p><strong>3.1 Information You Provide Directly</strong></p>
          <ul>
            <li>Name, email address, and phone number</li>
            <li>Self-reported academic information (e.g., major, classification) submitted voluntarily in membership or officer applications</li>
            <li>Event registration details, including RSVP responses and accessibility accommodation requests</li>
            <li>Content of messages submitted through contact, application, or feedback forms</li>
            <li>Payment or donation information where applicable; such transactions are processed by a third-party payment processor, and Comet Foundry does not collect or store full payment card details</li>
          </ul>
          <p><strong>3.2 Information Collected Automatically</strong></p>
          <p>As of the Effective Date, the Site does not use analytics or tracking software. If Comet Foundry adopts an analytics platform in the future, it will use Google Analytics and update this Policy accordingly, including opt-out information.</p>
          <p><strong>3.3 Information from Third Parties</strong></p>
          <p>Publicly available professional information (for example, from LinkedIn) that a member voluntarily elects to include in an organizational directory or mentorship profile.</p>

          <h2>4. How We Use Information</h2>
          <ul>
            <li>To administer membership records, officer elections, and organizational operations</li>
            <li>To communicate about events, workshops, mentorship, and internship opportunities</li>
            <li>To coordinate mentorship and internship-pipeline activities with our founding Industry Partner, Resilient Privacy Inc., limited strictly to members who affirmatively opt in</li>
            <li>To respond to inquiries and maintain the security of the Site</li>
          </ul>
          <p>Comet Foundry does not use personal information for automated decision-making with legal or similarly significant effects.</p>

          <h2>5. Disclosure of Information</h2>
          <p>Comet Foundry does not sell personal information. Information may be disclosed only as follows:</p>
          <table class="legal-table">
            <thead><tr><th>Recipient</th><th>Purpose</th></tr></thead>
            <tbody>
              <tr><td>Resilient Privacy Inc. (Industry Partner)</td><td>Mentorship coordination and internship referrals, limited to opted-in members</td></tr>
              <tr><td>Operational service providers</td><td>Email delivery, form processing, and hosting, under confidentiality obligations</td></tr>
              <tr><td>Legal authorities</td><td>Where required by law, subpoena, or court order, or to protect the rights or safety of Comet Foundry, its members, or others</td></tr>
            </tbody>
          </table>
          <p>Resilient Privacy Inc. holds a non-voting, advisory role within Comet Foundry's governance structure and has no standing access to member information beyond programs a member has voluntarily joined.</p>

          <h2>6. Data Retention</h2>
          <p>Information is retained only as long as reasonably necessary for the purposes described in this Policy or as required by law. Information relating to inactive members is archived or deleted within a reasonable period following the end of active involvement.</p>

          <h2>7. Data Security</h2>
          <p>Comet Foundry implements reasonable administrative and technical safeguards to protect information against unauthorized access, use, or disclosure. No method of electronic storage or transmission is completely secure, and Comet Foundry cannot guarantee absolute security.</p>

          <h2>8. Your Rights and Choices</h2>
          <ul>
            <li>Request access to, correction of, or deletion of your personal information</li>
            <li>Opt out of non-essential communications at any time</li>
            <li>Withdraw consent to having your information shared with Resilient Privacy Inc. without affecting your underlying membership</li>
          </ul>
          <p>Requests may be submitted to security@cometfoundry.com.</p>

          <h2>9. Children's Privacy</h2>
          <p>The Services are not directed at children under 13, and Comet Foundry does not knowingly collect information from children under 13.</p>

          <h2>10. Third-Party Links</h2>
          <p>The Site may link to third-party websites. Comet Foundry is not responsible for the privacy practices of any linked third-party site.</p>

          <h2>11. Changes to This Policy</h2>
          <p>Comet Foundry may revise this Policy from time to time. Material changes will be posted on this page with a revised "Last Updated" date. Continued use of the Services constitutes acceptance of the revised Policy.</p>

          <div class="legal-contact">
            Comet Foundry<br>The University of Texas at Dallas<br>security@cometfoundry.com
          </div>
""")

terms_of_use_body = legal_shell("Terms of Use", "EFFECTIVE DATE: AUGUST 1, 2026 &nbsp;|&nbsp; LAST UPDATED: AUGUST 1, 2026", """
          <h2>1. Acceptance of Terms</h2>
          <p>These Terms of Use ("Terms") govern access to and use of cometfoundry.com (the "Site"), operated by Comet Foundry, a registered student organization at the University of Texas at Dallas ("UT Dallas"). By accessing or using the Site, you agree to be bound by these Terms. If you do not agree, do not access or use the Site.</p>

          <h2>2. About Comet Foundry</h2>
          <p>Comet Foundry is a student-led innovation, entrepreneurship, and technology organization registered through the UT Dallas Student Organization Center (SOC). Comet Foundry maintains full independence in its programming and governance decisions. Resilient Privacy Inc. serves as Comet Foundry's founding Industry Partner in a non-voting, advisory capacity only and does not direct or control Comet Foundry's decisions.</p>

          <h2>3. Eligibility</h2>
          <p>The Site is publicly accessible. Membership, officer, and voting roles are governed exclusively by the Comet Foundry Constitution and Bylaws and are reserved for currently enrolled UT Dallas students on the basis of self-attestation. Consistent with FERPA, Comet Foundry does not verify enrollment status through UT Dallas or SOC records.</p>

          <h2>4. Acceptable Use</h2>
          <ul>
            <li>Provide accurate information in any form submitted through the Site</li>
            <li>Use the Site only for lawful purposes</li>
            <li>Not disrupt, interfere with, or attempt unauthorized access to the Site</li>
            <li>Not scrape, copy, or redistribute Site content without written permission</li>
          </ul>

          <h2>5. Intellectual Property</h2>
          <p>The Comet Foundry name, logo, and Site content are the property of Comet Foundry or its licensors and may not be reproduced or used commercially without prior written consent.</p>

          <h2>6. User Submissions</h2>
          <p>Content you submit to the Site grants Comet Foundry a limited, non-exclusive license to use that content for organizational operations. You retain ownership of your submissions.</p>

          <h2>7. No Guarantee of Outcomes</h2>
          <p>Comet Foundry does not guarantee admission to any program, internship placement, mentorship match, funding, or any specific outcome from participation in its Services.</p>

          <h2>8. Assumption of Risk</h2>
          <p>Participation in Comet Foundry events, workshops, and activities is voluntary. Each participant assumes full responsibility for their own participation and safety, and agrees to follow all applicable UT Dallas policies and event guidelines.</p>

          <h2>9. Disclaimers</h2>
          <p>The Site and its content are provided "as is" and "as available," without warranties of any kind, express or implied, including warranties of merchantability, fitness for a particular purpose, and non-infringement. Comet Foundry does not warrant that the Site will be uninterrupted, error-free, or secure.</p>

          <h2>10. Limitation of Liability</h2>
          <p>To the fullest extent permitted by law, Comet Foundry, its officers, members, volunteers, and Resilient Privacy Inc. (collectively, the "Comet Foundry Parties") shall not be liable for any indirect, incidental, special, consequential, or punitive damages, or any loss of data, revenue, or goodwill, arising out of or related to use of the Site or participation in Comet Foundry activities, even if advised of the possibility of such damages.</p>

          <h2>11. Indemnification</h2>
          <p>You agree to indemnify, defend, and hold harmless the Comet Foundry Parties from and against any claims, liabilities, damages, losses, and expenses, including reasonable attorneys' fees, arising out of or related to your use of the Site, your violation of these Terms, or your participation in Comet Foundry activities.</p>

          <h2>12. Organizational Independence</h2>
          <p>Comet Foundry is governed by its own Constitution and Bylaws, with all governance and voting authority resting exclusively with its enrolled-student officers. Nothing on the Site constitutes an endorsement by UT Dallas beyond Comet Foundry's official SOC registration status.</p>

          <h2>13. Termination</h2>
          <p>Comet Foundry reserves the right to suspend or restrict access to the Site for any user who violates these Terms.</p>

          <h2>14. Governing Law</h2>
          <p>These Terms are governed by the laws of the State of Texas, without regard to conflict-of-laws principles.</p>

          <h2>15. Severability</h2>
          <p>If any provision of these Terms is held unenforceable, the remaining provisions will remain in full force and effect.</p>

          <h2>16. Changes to These Terms</h2>
          <p>Comet Foundry may revise these Terms from time to time. Continued use of the Site following posted changes constitutes acceptance of the revised Terms.</p>

          <div class="legal-contact">
            Comet Foundry<br>The University of Texas at Dallas<br>security@cometfoundry.com
          </div>
""")

write("privacy-policy.html", "Privacy Policy", "privacy-policy", privacy_policy_body)
write("terms-of-use.html", "Terms of Use", "terms-of-use", terms_of_use_body)

print("done")
