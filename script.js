// ---- Lab door ----
const door = document.getElementById('door');
const openBtn = document.getElementById('open-btn');
const doorStatus = document.getElementById('door-status');
const main = document.getElementById('main');

if (openBtn) {
  openBtn.addEventListener('click', () => {
    doorStatus.innerHTML = '<span class="dot"></span>LAB STATUS: OPEN ✓';
    doorStatus.classList.add('open');
    openBtn.textContent = 'OPENING...';
    setTimeout(() => {
      door.classList.add('open');
      main.classList.add('ready');
      sessionStorage.setItem('labDoorOpen', '1');
    }, 350);
  });
}

// Skip the door animation on subsequent page navigations within the same session
if (sessionStorage.getItem('labDoorOpen') === '1' && door) {
  door.classList.add('open');
  main.classList.add('ready');
  door.style.transition = 'none';
}

// ---- I'm bored button ----
const ideas = [
  'Build something.',
  'Find a teammate.',
  'Go to an event.',
  'Start a stupid idea.',
  'Ask someone smarter than you.',
  'Touch grass.'
];
const boredBtn = document.getElementById('bored-btn');
const boredPopup = document.getElementById('bored-popup');
const boredResult = document.getElementById('bored-result');
let lastIdea = -1;

if (boredBtn) {
  boredBtn.addEventListener('click', () => {
    let i = Math.floor(Math.random() * ideas.length);
    if (i === lastIdea) i = (i + 1) % ideas.length;
    lastIdea = i;
    boredResult.textContent = ideas[i];
    boredPopup.classList.add('show');
  });

  document.addEventListener('click', (e) => {
    if (!boredPopup.contains(e.target) && e.target !== boredBtn) {
      boredPopup.classList.remove('show');
    }
  });
}

// ---- Active nav link ----
(function highlightNav() {
  const current = document.body.getAttribute('data-page');
  if (!current) return;
  document.querySelectorAll('.nav-links a, .mobile-menu a').forEach(a => {
    if (a.getAttribute('data-nav') === current) a.classList.add('active');
  });
})();

// ---- Mobile menu toggle ----
const navToggle = document.getElementById('nav-toggle');
const mobileMenu = document.getElementById('mobile-menu');
if (navToggle && mobileMenu) {
  navToggle.addEventListener('click', () => {
    const open = mobileMenu.classList.toggle('open');
    navToggle.textContent = open ? '✕' : '☰';
    navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
}

// ---- Events calendar (Events page only) ----
const CAL_EVENTS = [
  { date: '2026-09-01', title: 'Foundry Kickoff Night', href: 'event-kickoff-night.html' }
];

(function initCalendar() {
  const grid = document.getElementById('cal-grid');
  if (!grid) return;
  const monthLabel = document.getElementById('cal-month-label');
  const today = new Date();
  let viewYear = today.getFullYear();
  let viewMonth = today.getMonth();

  function render() {
    grid.innerHTML = '';
    ['SUN','MON','TUE','WED','THU','FRI','SAT'].forEach(d => {
      const el = document.createElement('div');
      el.className = 'cal-dow';
      el.textContent = d;
      grid.appendChild(el);
    });

    const firstOfMonth = new Date(viewYear, viewMonth, 1);
    const startDow = firstOfMonth.getDay();
    const gridStart = new Date(viewYear, viewMonth, 1 - startDow);

    for (let i = 0; i < 42; i++) {
      const cellDate = new Date(gridStart.getFullYear(), gridStart.getMonth(), gridStart.getDate() + i);
      const cell = document.createElement('div');
      cell.className = 'cal-cell';
      if (cellDate.getMonth() !== viewMonth) cell.classList.add('muted');
      if (cellDate.toDateString() === today.toDateString()) cell.classList.add('today');

      const num = document.createElement('span');
      num.className = 'date-num';
      num.textContent = cellDate.getDate();
      cell.appendChild(num);

      const iso = cellDate.getFullYear() + '-' + String(cellDate.getMonth()+1).padStart(2,'0') + '-' + String(cellDate.getDate()).padStart(2,'0');
      CAL_EVENTS.filter(e => e.date === iso).forEach(e => {
        const pill = document.createElement('a');
        pill.className = 'cal-pill';
        pill.textContent = e.title;
        pill.href = e.href || 'javascript:void(0)';
        cell.appendChild(pill);
      });

      grid.appendChild(cell);
    }
    monthLabel.textContent = firstOfMonth.toLocaleString('en-US', { month: 'long', year: 'numeric' });
  }

  document.getElementById('cal-today')?.addEventListener('click', () => { viewYear = today.getFullYear(); viewMonth = today.getMonth(); render(); });
  document.getElementById('cal-prev')?.addEventListener('click', () => { viewMonth -= 1; if (viewMonth < 0) { viewMonth = 11; viewYear -= 1; } render(); });
  document.getElementById('cal-next')?.addEventListener('click', () => { viewMonth += 1; if (viewMonth > 11) { viewMonth = 0; viewYear += 1; } render(); });

  render();
})();

// ---- Add to calendar: Outlook deeplink + .ics download ----
const outlookLink = document.getElementById('cal-outlook-link');
if (outlookLink) {
  const params = new URLSearchParams({
    subject: 'Foundry Kickoff Night',
    startdt: '2026-09-01T19:00:00',
    enddt: '2026-09-01T21:00:00',
    location: 'UT Dallas — Lab 01',
    body: "First open house of the semester. Tour the space, pitch a half-formed idea, find someone to build it with."
  });
  outlookLink.href = 'https://outlook.office.com/calendar/0/deeplink/compose?' + params.toString();
}

function pad2(n) { return String(n).padStart(2, '0'); }
document.getElementById('add-cal-btn')?.addEventListener('click', () => {
  const ics = [
    'BEGIN:VCALENDAR',
    'VERSION:2.0',
    'PRODID:-//Comet Foundry//Events//EN',
    'BEGIN:VEVENT',
    'UID:kickoff-night-2026@cometfoundry.org',
    'DTSTART:20260901T190000',
    'DTEND:20260901T210000',
    'SUMMARY:Foundry Kickoff Night',
    'LOCATION:UT Dallas — Lab 01',
    'DESCRIPTION:First open house of the semester. Tour the space\\, pitch a half-formed idea\\, find someone to build it with.',
    'END:VEVENT',
    'END:VCALENDAR'
  ].join('\r\n');
  const blob = new Blob([ics], { type: 'text/calendar;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'foundry-kickoff-night.ics';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
});

// ---- Demo Day: title reveal on scroll into view ----
(function initDemoDayReveal() {
  try {
  const title = document.getElementById('demoday-title');
  if (!title) return;
  const reduceMotion = typeof window.matchMedia === 'function' && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (reduceMotion) {
    title.classList.add('revealed');
    return;
  }

  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.35 });

  io.observe(title);
  } catch (e) { console.warn('Demo Day reveal animation skipped:', e); }
})();
