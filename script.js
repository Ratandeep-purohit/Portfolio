// =============================================
// PORTFOLIO SCRIPT v4.0
// =============================================

document.addEventListener('DOMContentLoaded', () => {

    // ─── 1. YEAR ─────────────────────────────
    const yr = document.getElementById('current-year');
    if (yr) yr.textContent = new Date().getFullYear();

    // ─── 2. THEME TOGGLE ─────────────────────
    const toggleBtn = document.getElementById('theme-toggle');
    const body = document.body;
    const saved = localStorage.getItem('theme');
    const prefersLight = window.matchMedia('(prefers-color-scheme: light)').matches;
    if (saved === 'light' || (!saved && prefersLight)) {
        body.classList.remove('dark-theme');
        body.classList.add('light-theme');
        if (toggleBtn) toggleBtn.querySelector('i').className = 'fas fa-sun';
    }
    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            const isLight = body.classList.toggle('light-theme');
            body.classList.toggle('dark-theme', !isLight);
            toggleBtn.querySelector('i').className = isLight ? 'fas fa-sun' : 'fas fa-moon';
            localStorage.setItem('theme', isLight ? 'light' : 'dark');
        });
    }

    // ─── 3. HEADER SCROLL ────────────────────
    const header = document.getElementById('header');
    if (header) {
        window.addEventListener('scroll', () => {
            header.classList.toggle('scrolled', window.scrollY > 50);
        }, { passive: true });
    }

    // ─── 4. MOBILE NAV ───────────────────────
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');
    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('open');
            navLinks.classList.toggle('open');
        });
        navLinks.querySelectorAll('a').forEach(a => {
            a.addEventListener('click', () => {
                hamburger.classList.remove('open');
                navLinks.classList.remove('open');
            });
        });
    }

    // ─── 5. ACTIVE NAV LINK ──────────────────
    const page = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-links a').forEach(a => {
        a.classList.toggle('active', a.getAttribute('href') === page ||
            (page === '' && a.getAttribute('href') === 'index.html'));
    });

    // ─── 6. TYPING ANIMATION ─────────────────
    const el = document.getElementById('typingText');
    if (el) {
        const words = ['Intelligent APIs.', 'Scalable Systems.', 'AI Solutions.', 'Beautiful UIs.', 'Fast Backends.'];
        let wi = 0, ci = 0, del = false;
        const type = () => {
            const w = words[wi];
            el.textContent = w.substring(0, del ? --ci : ++ci);
            let speed = del ? 45 : 95;
            if (!del && ci === w.length) { del = true; speed = 2200; }
            else if (del && ci === 0) { del = false; wi = (wi + 1) % words.length; speed = 450; }
            setTimeout(type, speed);
        };
        setTimeout(type, 1200);
    }

    // ─── 7. COUNTER ANIMATION ─────────────────
    const animateCounter = (el) => {
        const target = +el.getAttribute('data-target');
        const duration = 1800;
        const start = performance.now();
        const step = (now) => {
            const pct = Math.min((now - start) / duration, 1);
            const eased = 1 - Math.pow(1 - pct, 3);
            el.textContent = Math.floor(eased * target) + (target >= 500 ? '+' : '+');
            if (pct < 1) requestAnimationFrame(step);
            else el.textContent = target + '+';
        };
        requestAnimationFrame(step);
    };

    // ─── 9. INTERSECTION OBSERVER ────────────
    const io = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            const el = entry.target;
            // AOS animations
            if (el.hasAttribute('data-aos')) el.classList.add('aos-in');
            // Counter
            if (el.classList.contains('stat-number')) animateCounter(el);
            obs.unobserve(el);
        });
    }, { threshold: 0.15 });

    document.querySelectorAll('[data-aos], .stat-number').forEach(el => io.observe(el));

    // ─── 10. PROJECT FILTER ──────────────────
    const filterBtns = document.querySelectorAll('.filter-btn');
    const cards = document.querySelectorAll('.project-card[data-category]');
    if (filterBtns.length && cards.length) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                const f = btn.dataset.filter;
                cards.forEach(c => {
                    const cats = c.dataset.category.split(' ');
                    const show = f === 'all' || cats.includes(f);
                    c.style.opacity = '0';
                    c.style.transform = 'translateY(20px)';
                    setTimeout(() => {
                        c.style.display = show ? 'flex' : 'none';
                        if (show) {
                            requestAnimationFrame(() => {
                                c.style.opacity = '1';
                                c.style.transform = 'translateY(0)';
                            });
                        }
                    }, 200);
                });
            });
        });
    }

    // ─── 11. SMOOTH SCROLL NAV ───────────────
    document.querySelectorAll('a[href^="#"]').forEach(a => {
        a.addEventListener('click', e => {
            const id = a.getAttribute('href').slice(1);
            const target = document.getElementById(id);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ─── 12. TILT ON ABOUT IMAGE ─────────────
    document.querySelectorAll('[data-tilt]').forEach(el => {
        el.addEventListener('mousemove', e => {
            const { left, top, width, height } = el.getBoundingClientRect();
            const rx = ((e.clientY - top) / height - 0.5) * -12;
            const ry = ((e.clientX - left) / width - 0.5) * 12;
            el.style.transform = `perspective(1000px) rotateX(${rx}deg) rotateY(${ry}deg) scale3d(1.02,1.02,1.02)`;
            el.style.transition = 'none';
        });
        el.addEventListener('mouseleave', () => {
            el.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale3d(1,1,1)';
            el.style.transition = 'transform .5s ease';
        });
    });
});
