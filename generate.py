import os

OUT = os.path.dirname(os.path.abspath(__file__))

OG_BASE_URL = "https://www.cometfoundry.com"

ORG_JSONLD = """  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Comet Foundry",
    "url": "https://www.cometfoundry.com/",
    "logo": "https://www.cometfoundry.com/assets/comet-foundry-logo.png",
    "email": "info@cometfoundry.com",
    "foundingDate": "2026",
    "founder": { "@type": "Person", "name": "Vishva Patel" },
    "sameAs": [
      "https://www.linkedin.com/company/cometfoundry/",
      "https://www.instagram.com/cometfoundry",
      "https://discord.com/invite/Hdg8VBFUW"
    ],
    "location": {
      "@type": "Place",
      "name": "UT Dallas",
      "address": { "@type": "PostalAddress", "addressLocality": "Richardson", "addressRegion": "TX", "addressCountry": "US" }
    }
  }
  </script>
"""

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{og_url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Comet Foundry">
<meta property="og:title" content="{page_title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{og_url}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:url" content="{og_url}">
<meta name="twitter:title" content="{page_title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og_image}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=IBM+Plex+Mono:wght@400;500;700&family=Caveat:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<link rel="icon" type="image/png" href="assets/favicon.png?v=4">
<link rel="icon" type="image/png" sizes="16x16" href="assets/icon-16.png">
<link rel="icon" type="image/png" sizes="32x32" href="assets/icon-32.png">
<link rel="apple-touch-icon" sizes="180x180" href="assets/icon-180.png">
<link rel="manifest" href="manifest.json">
<meta name="theme-color" content="#15161A">
{org_jsonld}</head>
<body data-page="{page}">

  <a class="skip-link" href="#main">Skip to content</a>

  <div id="door" role="dialog" aria-modal="true" aria-labelledby="door-title">
    <div class="door-status mono" id="door-status"><span class="dot"></span>LAB STATUS: CLOSED</div>
    <div id="door-title">COMET<br>FOUNDRY</div>
    <button id="open-btn">OPEN LAB →</button>
    <div id="door-meta" class="mono">EST. 2026 / UT DALLAS / LAB 01</div>
  </div>

  <main id="main">
    <header class="nav">
      <div class="wrap">
        <a class="brand-mark" href="index.html"><img src="assets/comet-foundry-logo.png" alt="Comet Foundry" class="nav-logo" width="400" height="357">COMET FOUNDRY</a>
        <nav class="nav-links">
          <a href="about.html" data-nav="about">About</a>
          <a href="programs.html" data-nav="programs">Programs</a>
          <a href="projects.html" data-nav="projects">Projects</a>
          <div class="nav-item-dropdown">
            <span class="nav-dropdown-label" data-nav="team">Team</span>
            <div class="nav-dropdown-menu">
              <a href="founder.html" data-nav="founder">Founder</a>
              <a href="team.html" data-nav="team">UTD Crew</a>
            </div>
          </div>
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
        <span class="mobile-menu-label">Team</span>
        <a href="founder.html" data-nav="founder" class="mobile-sub-link">↳ Founder</a>
        <a href="team.html" data-nav="team" class="mobile-sub-link">↳ UTD Crew</a>
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
            <img src="assets/comet-foundry-logo.png" alt="Comet Foundry" class="footer-logo" width="400" height="357">
            <h4>Comet Foundry</h4>
            <p class="footer-brand-line">UT Dallas / Fall 2026</p>
            <p class="footer-brand-line hand">Someone had to try. :)</p>
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
  <script defer src="/_vercel/insights/script.js"></script>
</body>
</html>
"""

DEFAULT_DESC = "A hacker house at UT Dallas. No perfect ideas. Just interesting ones."

def write(fname, title, page, body, desc=None, full_title=None):
    desc = desc or DEFAULT_DESC
    page_title = full_title or f"{title} — Comet Foundry"
    og_url = OG_BASE_URL + ("/" if fname == "index.html" else "/" + fname)
    og_image = OG_BASE_URL + "/assets/og-image.png"
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(HEAD.format(page_title=page_title, page=page, desc=desc, og_url=og_url, og_image=og_image, org_jsonld=ORG_JSONLD))
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
          <span class="tag">BORN AT UTD</span>
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
          <h2>The <span class="hand" style="font-size:1.15em; color:var(--flask);">CF</span>, in one paragraph</h2>
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
              <li><span>Foundry Kickoff Night</span><span class="v">SEP 01</span></li>
              <li><span>Peer matching for team formation</span><span class="v">TBD</span></li>
              <li><span>Open critique nights</span><span class="v">TBD</span></li>
              <li><span>Alumni founder network</span><span class="v">TBD</span></li>
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

    <!-- ================= HACKER CAMPUS MAP ================= -->
    <section class="campus">
      <div class="campus-inner">
        <div class="campus-stage">
          <div class="campus-map" aria-hidden="true">
<img class="campus-map-svg" src="assets/campus-map.svg" alt="Map of the continental United States with Comet Foundry's node in Texas" width="950" height="580" loading="lazy">
          </div>
          <h2 class="campus-title">THE<br>HACKER<br>CAMPUS</h2>
          <div class="campus-cta">
            <span class="campus-cta-note hand">not in your school yet?</span>
            <a class="campus-cta-btn" href="https://forms.cloud.microsoft/r/FPR6PcbQaN" target="_blank" rel="noopener">start a node →</a>
          </div>
        </div>
      </div>
    </section>

    <section class="join">
      <div class="wrap">
        <div class="sec-head center">
          <span class="num mono">EXP 002 / GET IN</span>
          <h2>Join The Foundry</h2>
          <p>One email. We'll tell you when the door's open.</p>
        </div>
        <form class="join-form" id="join-form">
          <input type="email" name="email" placeholder="you@utdallas.edu" required aria-label="Email address">
          <input type="text" name="company" class="hp-field" tabindex="-1" autocomplete="off" aria-hidden="true">
          <button type="submit">SUBSCRIBE →</button>
        </form>
        <div class="join-note">NO SPAM. NO PERFECT IDEAS. JUST INTERESTING ONES. &nbsp;·&nbsp; <a href="https://forms.cloud.microsoft/pages/responsepage.aspx?id=HR0ojU2c90uxbgMtFd6fbIhHjy7i2rpHt7VcaeT3yedUMkQwTTU4TkpUNFczMVQzS0cwUUVaWEw0WC4u&route=shorturl&b2b=true" target="_blank" rel="noopener" style="color:var(--ink-soft);">Full application →</a></div>
      </div>
    </section>
"""
write("index.html", "Home", "home", home_body, desc="A hacker house at UT Dallas. No perfect ideas. Just interesting ones.", full_title="Comet Foundry — UT Dallas")

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

    <section class="tight">
      <div class="wrap">
        <div class="sec-head">
          <span class="num">FAQ</span>
          <h2>Questions People Actually Ask</h2>
        </div>
        <div class="faq-list">
          <details class="faq-item">
            <summary>What is Comet Foundry?</summary>
            <p>A hacker house at UT Dallas — a physical space and community for students to build projects, ship ideas, and find people to build them with. It's technically a student org, but it doesn't run like one: no recurring meetings, no permission required to start something.</p>
          </details>
          <details class="faq-item">
            <summary>Do I need to be a CS major to join?</summary>
            <p>No. CS major, art major, undeclared — if you want to build, there's a seat. We care what you want to make, not what's on your résumé.</p>
          </details>
          <details class="faq-item">
            <summary>How do I apply?</summary>
            <p>Head to the <a href="apply.html">Apply page</a> and tell us what you want to build — that's most of the application.</p>
          </details>
          <details class="faq-item">
            <summary>Where is Comet Foundry located?</summary>
            <p>UT Dallas, Lab 01.</p>
          </details>
          <details class="faq-item">
            <summary>How do I find out about upcoming events?</summary>
            <p>Check the <a href="events.html">Events page</a> or RSVP to <a href="event-kickoff-night.html">Foundry Kickoff Night</a>, the first open house of the semester.</p>
          </details>
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

    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is Comet Foundry?",
          "acceptedAnswer": { "@type": "Answer", "text": "A hacker house at UT Dallas — a physical space and community for students to build projects, ship ideas, and find people to build them with. It's technically a student org, but it doesn't run like one: no recurring meetings, no permission required to start something." }
        },
        {
          "@type": "Question",
          "name": "Do I need to be a CS major to join?",
          "acceptedAnswer": { "@type": "Answer", "text": "No. CS major, art major, undeclared — if you want to build, there's a seat. We care what you want to make, not what's on your résumé." }
        },
        {
          "@type": "Question",
          "name": "How do I apply?",
          "acceptedAnswer": { "@type": "Answer", "text": "Head to the Apply page and tell us what you want to build — that's most of the application." }
        },
        {
          "@type": "Question",
          "name": "Where is Comet Foundry located?",
          "acceptedAnswer": { "@type": "Answer", "text": "UT Dallas, Lab 01." }
        },
        {
          "@type": "Question",
          "name": "How do I find out about upcoming events?",
          "acceptedAnswer": { "@type": "Answer", "text": "Check the Events page or RSVP to Foundry Kickoff Night, the first open house of the semester." }
        }
      ]
    }
    </script>
"""
write("about.html", "About", "about", about_body, desc="Comet Foundry started because the good ideas at UT Dallas kept dying in group chats instead of becoming things. Here's the origin story.")

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
write("programs.html", "Programs", "programs", programs_body, desc="Four labs, not departments: Build, Think, Network, and After Hours. Drop into whichever matches what you're in the mood for this week.")

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
write("projects.html", "Projects", "projects", projects_body, desc="Member-built projects from Comet Foundry, UT Dallas's hacker house. This wall is just getting started — check back as things ship.")

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
write("team.html", "Team", "team", team_body, desc="Meet the Comet Foundry team — Executive Board and Officer seats, most still open. Apply if one fits you.")

# ---------------- FOUNDER ----------------
founder_body = """
    <section class="founder-hero">
      <div class="wrap">
        <div class="breadcrumb"><a href="index.html">Home</a> / <a href="team.html">Team</a> / Founder</div>
        <span class="eyebrow-label">FIELD NOTE #001</span>
        <h1>The Founder</h1>

        <div class="founder-intro">
          <div class="founder-portrait">
            <img src="assets/vishva-patel.jpg" alt="Vishva Patel" width="760" height="760">
          </div>
          <div class="founder-meta">
            <h2>Vishva Patel</h2>
            <div class="role">FOUNDER / COMET FOUNDRY</div>
            <div class="sub">UT DALLAS / SPRING 25 ALUMNUS</div>
            <p class="intro"><strong>Somewhere in this hacker house, the next billionaire is debugging their first prototype. I built the house.</strong><br>Founder &amp; Investor, Comet Foundry || 2x Founder || 10+ Years Cybersecurity || UTD Alumni &amp; Former GSA President</p>
            <span class="brand-line hand">Someone had to try. :)</span>
          </div>
        </div>
      </div>
    </section>

    <section class="founder-section">
      <div class="wrap">
        <span class="tag-label">FOUNDER'S LETTER</span>
        <h2 class="big">Why I Started This</h2>
        <div class="letter-card">
          <div class="founder-letter">
            <p>When I founded Comet Foundry, I wasn't trying to create another student organization. I wanted to build a place where ideas don't die in group chats.</p>
            <p>UT Dallas is filled with ambitious people, brilliant ideas, and future founders. The challenge isn't talent — it's creating the environment where talent can collide, collaborate, and build.</p>
            <p>My vision is simple: make UTD the best place in the country for students to start something meaningful. A place where builders find co-founders, ideas become products, and students graduate not just with a degree, but with impact.</p>
            <p>Comet Foundry exists for those willing to take a chance on an idea, learn by building, and create the future instead of waiting for it.</p>
          </div>
          <div class="letter-signature">
            <span class="letter-signoff hand">— Vishva</span>
            <div class="letter-author">
              <img src="assets/vishva-patel.jpg" alt="Vishva Patel" class="letter-avatar" width="760" height="760">
              <div>
                <div class="letter-author-name">Vishva Patel</div>
                <div class="letter-author-role">Founder, Comet Foundry</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="founder-section founder-quote">
      <div class="wrap">
        <span class="tag-label" style="text-align:left;">MY BET</span>
        <blockquote>"I believe the best student experiences don't start with a perfectly planned idea. They start with someone saying: 'What if we tried?'"</blockquote>
        <p class="vision-text">Comet Foundry should become a place where students don't have to wait for permission to start something. A place where someone can walk in with an unfinished idea, meet someone who wants to help, and actually make something.</p>
        <p class="vision-text">The goal isn't simply to run more student events. The goal is to build a culture — people who build, question, experiment, collaborate, and keep showing up. <span class="mono" style="font-size:13px; color:var(--ink-soft);">STATUS: BUILDING</span></p>
      </div>
    </section>

    <section class="founder-section founder-note-to-students">
      <div class="wrap">
        <span class="tag-label">A NOTE TO STUDENTS</span>
        <h2 class="big">A Note To Students</h2>
        <div class="founder-letter">
          <p>You don't need to be the smartest person in the room. You don't need a startup. You don't need a five-person team. You don't need a perfectly polished idea.</p>
          <p>You just need to show up.</p>
          <p>Show up curious. Find something worth building. Find someone worth building with. Ask a question you don't know the answer to. Try something that might fail.</p>
          <p>And if it doesn't work — good. That's what the lab is for.</p>
          <p>Comet Foundry isn't supposed to be a place where you already have everything figured out. It's supposed to be a place where you figure it out together.</p>
          <p>So bring the weird idea. Bring the half-built project. Bring the question you've been sitting on. We'll see what happens.</p>
        </div>
        <div class="founder-signoff">
          <div class="see-you">See You In The Lab.</div>
          <div class="dash-vishva">— VISHVA</div>
        </div>
      </div>
    </section>

    <section class="founder-contact">
      <div class="wrap">
        <span class="tag-label" style="text-align:center;">WANT TO TALK?</span>
        <div class="founder-contact-name">Vishva Patel</div>
        <div class="founder-contact-role">FOUNDER / COMET FOUNDRY</div>
        <div class="founder-contact-rows">
          <div>
            <span class="row-label">EMAIL</span>
            <a href="mailto:vishva.patel@cometfoundry.com">vishva.patel@cometfoundry.com</a>
          </div>
          <div>
            <span class="row-label">LINKEDIN</span>
            <a class="founder-linkedin" href="https://www.linkedin.com/in/vishva-vp/" target="_blank" rel="noopener" aria-label="Vishva Patel on LinkedIn">
              <svg viewBox="0 0 24 24"><path d="M4.98 3.5C4.98 4.88 3.87 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1s2.48 1.12 2.48 2.5zM.5 8h4v15h-4V8zm7.5 0h3.8v2.05h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1V23h-4v-6.9c0-1.65-.03-3.77-2.3-3.77-2.3 0-2.65 1.8-2.65 3.65V23h-4V8z"/></svg>
            </a>
          </div>
        </div>
      </div>
    </section>
"""
write("founder.html", "Founder", "founder", founder_body, desc="Vishva Patel, founder of Comet Foundry — a 2x founder and cybersecurity professional building a hacker house at UT Dallas.")


# ---------------- PARTNERS ----------------
def partner_card(grad, name, blurb, url=None, logo=None, logo_w=500, logo_h=552):
    link_html = f'<a class="card-link" href="{url}" target="_blank" rel="noopener">Visit site →</a>' if url else ""
    media_html = f'<img src="{logo}" alt="{name}" width="{logo_w}" height="{logo_h}">' if logo else ""
    return f"""
          <div class="partner-card">
            <div class="card-media {grad}">{media_html}</div>
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
    partner_card("", "RESILIENT PRIVACY Inc.", '<a href="https://www.resilientprivacy.com/?utm_source=chatgpt.com" target="_blank" rel="noopener">Resilient Privacy</a> is building an AI-native, unified platform for IT and cybersecurity operations.', "https://www.resilientprivacy.com/?utm_source=chatgpt.com", "assets/resilient-privacy-logo.jpg") + \
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
        <a class="rsvp-btn" href="https://forms.cloud.microsoft/pages/responsepage.aspx?id=HR0ojU2c90uxbgMtFd6fbIhHjy7i2rpHt7VcaeT3yedUNVNQVFY2NUpKWkVSTDFZR01LQjlRUTdJQi4u&route=shorturl" target="_blank" rel="noopener" style="background:var(--ink); color:var(--paper);">GET IN TOUCH →</a>
      </div>
    </section>
"""
write("partners.html", "Partners", "partners", partners_body, desc="Comet Foundry's industry partners fund experiments, send mentors, and show up for demo nights. Meet Resilient Privacy Inc. and others.")

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
write("events.html", "Events", "events", events_body, desc="Build sprints, critique nights, demo nights, and Foundry Kickoff Night — see what's happening at Comet Foundry, UT Dallas.")

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
        <a class="rsvp-btn" href="https://forms.cloud.microsoft/pages/responsepage.aspx?id=HR0ojU2c90uxbgMtFd6fbIhHjy7i2rpHt7VcaeT3yedUOVlFMEpKR0dYMDhLUzAyMjQ2QklROFVaVC4u&route=shorturl" target="_blank" rel="noopener" style="background:var(--ink); color:var(--paper);">RSVP →</a>
      </div>
    </section>

    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Event",
      "name": "Foundry Kickoff Night",
      "description": "First open house of the semester. Tour the space, pitch a half-formed idea out loud, and find someone to build it with.",
      "startDate": "2026-09-01T19:00:00-05:00",
      "endDate": "2026-09-01T21:00:00-05:00",
      "eventStatus": "https://schema.org/EventScheduled",
      "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
      "location": {
        "@type": "Place",
        "name": "UT Dallas — Lab 01",
        "address": { "@type": "PostalAddress", "addressLocality": "Richardson", "addressRegion": "TX", "addressCountry": "US" }
      },
      "organizer": { "@type": "Organization", "name": "Comet Foundry", "url": "https://www.cometfoundry.com/" }
    }
    </script>
"""
write("event-kickoff-night.html", "Kickoff Night", "events", event_detail_body, desc="Foundry Kickoff Night — the first open house of the semester at Comet Foundry, UT Dallas. Tour the space, pitch an idea, find a team.")

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

def blog_post_shell(title, date_label, iso_date, paragraphs, href):
    body_html = "\n".join(f"          <p>{p}</p>" for p in paragraphs)
    ld = f"""
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BlogPosting",
      "headline": "{title}",
      "datePublished": "{iso_date}",
      "author": {{ "@type": "Person", "name": "Vishva Patel" }},
      "publisher": {{ "@type": "Organization", "name": "Comet Foundry", "url": "https://www.cometfoundry.com/" }},
      "mainEntityOfPage": "https://www.cometfoundry.com/{href}"
    }}
    </script>"""
    return f"""
    <section class="page-hero">
      <div class="wrap">
        <div class="breadcrumb"><a href="index.html">Home</a> / <a href="blog.html">Blog</a> / {title}</div>
        <h1>{title}</h1>
      </div>
    </section>

    <section class="tight">
      <div class="wrap">
        <div class="legal-body">
          <div class="legal-effective">{date_label} &nbsp;|&nbsp; THINK LAB</div>
{body_html}
        </div>
        <div style="max-width:760px; margin:44px auto 0; padding-top:24px; border-top:1px solid var(--line);">
          <a class="lab-link mono" href="blog.html" style="color:var(--ink-soft); border-bottom:1px solid var(--line); text-decoration:none; font-size:13px;">← Back to all posts</a>
        </div>
      </div>
    </section>
{ld}
"""

blog_post_1 = blog_post_shell(
    "The 9-5 Felt Safe. It Wasn't.",
    "AUG 15, 2026",
    "2026-08-15",
    [
        "A friend of mine got laid off last year. Six years at the same company, good reviews every cycle, never missed a deadline. Then one Tuesday morning, a 15-minute call, and it was over. No warning, no say in it, no plan B because he'd never needed one — the job was the plan.",
        "I used to think startups were the risky path and a steady job was the safe one. I don't think that anymore. A job is a bet you make on one company, one manager, one budget cycle, and you don't get a vote in any of it. If it goes well, you get a raise. If it doesn't, you get an email.",
        "Building something of your own is a different kind of risk — the kind where the outcome is actually tied to your effort. It's harder in the short term. There's no bi-weekly paycheck telling you you're doing fine. But over a longer stretch, you end up owning something instead of renting your income from someone else.",
        "I'm not saying everyone should quit their job tomorrow. Most people can't, and that's a real constraint, not a mindset problem. What I am saying is: stop assuming the safe-looking path is actually the safe one. Ask what happens to you the day the company decides it doesn't need you anymore. If the answer is \"not much,\" that's worth sitting with.",
        "That's part of why we started Comet Foundry. Not everyone in the house has quit their job. Some are building nights and weekends, testing the waters before jumping. That's fine — the point isn't recklessness. The point is not mistaking comfort for security.",
    ],
    "blog-9-5-felt-safe.html",
)
write("blog-9-5-felt-safe.html", "The 9-5 Felt Safe. It Wasn't.", "blog", blog_post_1, desc="A steady job isn't the safe path it looks like — it's a bet on one company, one manager, one budget cycle you don't get a vote in. Notes from Comet Foundry's Think Lab.")

blog_post_2 = blog_post_shell(
    "Nobody Tells You the First Idea Usually Doesn't Work",
    "AUG 08, 2026",
    "2026-08-08",
    [
        "When I started my first company, I thought I had it figured out. I hadn't. It didn't work, and for a while that felt like proof I wasn't cut out for this.",
        "Looking back, almost everyone I know who's built something real has a version of this story — an idea that didn't land, a launch nobody showed up for, months spent on something that quietly died. The founders you hear about are usually on their second or third attempt by the time anyone's paying attention. You just never hear about attempt one.",
        "That gap between the story you're told and the reality is what makes people quit too early. They assume struggling on the first try means they're not built for this, so they go back to something safer before they get the chance to actually get good at it.",
        "Nobody's born knowing how to hire, how to talk to a customer who hates your product, or how to keep going after a partner backs out. You learn that by doing it badly the first time and less badly the second. That's not failure — that's just what the process looks like from the inside.",
        "This is the actual reason a house like Comet Foundry matters more than another mentorship program or another pitch deck template. Put people in the same kitchen while they're on attempt one, two, and three at the same time, and the lesson passes between them faster than any advice could. You watch someone else survive their bad idea, and it makes yours feel a lot less like the end of the road.",
    ],
    "blog-first-idea-doesnt-work.html",
)
write("blog-first-idea-doesnt-work.html", "Nobody Tells You the First Idea Usually Doesn't Work", "blog", blog_post_2, desc="Almost everyone who's built something real has a first attempt that quietly died. You just never hear about it. Notes from Comet Foundry's Think Lab.")

blog_post_3 = blog_post_shell(
    "We Trained a Generation to Follow Instructions. The World Needs People Who Can Build.",
    "AUG 01, 2026",
    "2026-08-01",
    [
        "I think about this a lot when I talk to students at UT Dallas — smart, capable people who can solve almost any problem you hand them, as long as someone else defines the problem first. That's not a knock on them. It's what school actually teaches: follow the instructions well, get the grade, repeat.",
        "Nobody hands you the muscle for the opposite — deciding what the problem even is, building something nobody asked for yet, being wrong in public until you're right. That skill isn't taught. It's practiced, usually by accident, usually by people who ended up around others doing the same thing.",
        "I don't think this is a small gap. As more of the predictable work — the kind school prepares you for — gets automated, the people who stay hard to replace are the ones who can build from nothing, not the ones who can execute instructions well. That shift is already happening. Most people just haven't felt it yet.",
        "I didn't get this muscle from a classroom. I got it from failing at my first company, from late nights during a hackathon that didn't even place first, from being around other people trying to build things and watching how they thought. Comet Foundry exists because I don't think that kind of learning should be an accident. It should be something people can walk into on purpose.",
        "You don't need permission to build something. You need a room where building is normal, and people around you who won't let you talk yourself out of it. That's the bet we're making with this house — that if you put enough people like that in one place, some of them are going to build something the rest of us will be talking about in a few years.",
    ],
    "blog-build-dont-follow.html",
)
write("blog-build-dont-follow.html", "We Trained a Generation to Follow Instructions. The World Needs People Who Can Build.", "blog", blog_post_3, desc="School teaches you to follow instructions well. Nobody teaches you to decide what the problem even is. Notes from Comet Foundry's Think Lab.")

blog_body = """
    <section class="page-hero">
      <div class="wrap">
        <div class="breadcrumb"><a href="index.html">Home</a> / Blog</div>
        <h1>Notes From The Lab</h1>
        <span class="hero-note hand">fresh from the lab</span>
        <p class="lede">Updates, postmortems, and the occasional controversial opinion from Think Lab.</p>
      </div>
    </section>

    <section class="tight">
      <div class="wrap">
        <div class="card-grid">""" + \
    post_card("", "AUG 15, 2026", "The 9-5 Felt Safe. It Wasn't.", "A friend got laid off after six years of good reviews. That's when I stopped thinking of a steady job as the safe path.", "blog-9-5-felt-safe.html") + \
    post_card("alt", "AUG 08, 2026", "Nobody Tells You the First Idea Usually Doesn't Work", "Almost everyone who's built something real has a first attempt that quietly died. You just never hear about it.", "blog-first-idea-doesnt-work.html") + \
    post_card("alt2", "AUG 01, 2026", "We Trained a Generation to Follow Instructions. The World Needs People Who Can Build.", "School teaches you to follow instructions well. Nobody teaches you to decide what the problem even is.", "blog-build-dont-follow.html") + """
        </div>
      </div>
    </section>
"""
write("blog.html", "Blog", "blog", blog_body, desc="Updates, postmortems, and the occasional controversial opinion from Comet Foundry's Think Lab.")

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
        <form class="apply-form" hidden>
          <div>
            <label for="apply-name">Name</label>
            <input type="text" id="apply-name" required>
          </div>
          <div>
            <label for="apply-email">Email</label>
            <input type="email" id="apply-email" required>
          </div>
          <div>
            <label for="apply-year">Major / Year</label>
            <input type="text" id="apply-year" placeholder="e.g. CS, Sophomore">
          </div>
          <div>
            <label for="apply-build">What do you want to build?</label>
            <textarea id="apply-build" placeholder="A rough idea is plenty."></textarea>
          </div>
          <div>
            <label for="apply-heard">How'd you hear about us?</label>
            <select id="apply-heard">
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
write("apply.html", "Apply", "apply", apply_body, desc="Apply to Comet Foundry, UT Dallas's hacker house. Tell us what you want to build — that's most of the application.")

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
          <p>Membership applications, officer applications, and event RSVPs are collected through Microsoft Forms rather than directly on the Site; see Section 3.4 for the full list of third-party service providers Comet Foundry uses.</p>
          <p><strong>3.2 Information Collected Automatically</strong></p>
          <p>The Site uses Vercel Web Analytics, a privacy-focused analytics service that does not use cookies and does not collect personally identifiable information. It records aggregate, anonymized usage data such as page views, referrer, and general geographic region (country/region level) to help us understand how the Site is used. Comet Foundry does not use any other analytics or advertising-tracking software.</p>
          <p><strong>3.3 Information from Third Parties</strong></p>
          <p>Publicly available professional information (for example, from LinkedIn) that a member voluntarily elects to include in an organizational directory or mentorship profile.</p>
          <p><strong>3.4 Third-Party Service Providers</strong></p>
          <p>Comet Foundry uses the following third-party services to operate the Site and process the information described above. Each processes information under its own privacy policy and terms:</p>
          <ul>
            <li><strong>Microsoft Forms</strong> — processes membership and officer applications, event RSVPs, and partner inquiry submissions.</li>
            <li><strong>Resend</strong> — delivers the email generated when someone submits the "Join The Foundry" email sign-up on the Site.</li>
            <li><strong>Vercel</strong> — hosts the Site and provides the Web Analytics service described in Section 3.2.</li>
          </ul>

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

write("privacy-policy.html", "Privacy Policy", "privacy-policy", privacy_policy_body, desc="How Comet Foundry collects, uses, and protects information for cometfoundry.com and related programs.")
write("terms-of-use.html", "Terms of Use", "terms-of-use", terms_of_use_body, desc="Terms governing use of the Comet Foundry website, cometfoundry.com, and related services.")

# ---------------- 404 ----------------
not_found_body = """
    <section class="page-hero">
      <div class="wrap">
        <div class="breadcrumb"><a href="index.html">Home</a> / Not Found</div>
        <h1>404</h1>
        <span class="hero-note hand">this experiment failed</span>
        <p class="lede">Nothing's built at this address. The page you're looking for either moved or never shipped.</p>
      </div>
    </section>

    <section class="tight">
      <div class="wrap" style="text-align:center;">
        <a class="rsvp-btn" href="index.html" style="background:var(--ink); color:var(--paper);">Back to home →</a>
      </div>
    </section>
"""
write("404.html", "Not Found", "404", not_found_body, desc="This page doesn't exist. Head back to the Comet Foundry homepage.")

print("done")
