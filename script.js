document.addEventListener('DOMContentLoaded', () => {

    // --- 1. Typing Animation ---
    const typingText = document.querySelector('.typing-text');
    const words = ["Software Developer", "Python Expert", "Tech Researcher", "Problem Solver"];
    let wordIndex = 0;
    let charIndex = 0;
    let isDeleting = false;

    function typeEffect() {
        const currentWord = words[wordIndex];

        if (isDeleting) {
            charIndex--;
        } else {
            charIndex++;
        }

        typingText.textContent = currentWord.substring(0, charIndex);

        // Dynamic speed
        let typeSpeed = isDeleting ? 100 : 200;

        if (!isDeleting && charIndex === currentWord.length) {
            isDeleting = true;
            typeSpeed = 2000; // Pause at end of word
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            wordIndex = (wordIndex + 1) % words.length;
            typeSpeed = 500;
        }

        setTimeout(typeEffect, typeSpeed);
    }
    typeEffect();


    // --- 2. Navbar Scroll Effect ---
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });


    // --- 3. Mobile Menu Toggle ---
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        hamburger.classList.toggle('toggle');
    });

    // Close menu when clicking a link
    document.querySelectorAll('.nav-links li a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            hamburger.classList.remove('toggle');
        });
    });


    // --- 4. Intersection Observer for Animations ---
    const observerOptions = {
        threshold: 0.2
    };

    const animateOnScroll = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Determine what element it is and animate
                if (entry.target.classList.contains('skill-bar')) {
                    const progressBar = entry.target.querySelector('.progress');
                    // Get width from inline style or calculate it based on class if preferred, 
                    // for now let's manually assume widths based on HTML logic modification or just attributes
                    // Simpler: let's rely on the CSS class names added in HTML (progress python -> 90%)
                    if (progressBar.classList.contains('python')) progressBar.style.width = '90%';
                    if (progressBar.classList.contains('java')) progressBar.style.width = '85%';
                    if (progressBar.classList.contains('cpp')) progressBar.style.width = '70%';
                }

                // General Fade In
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';

                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe Skill Bars
    document.querySelectorAll('.skill-bar').forEach(bar => {
        animateOnScroll.observe(bar);
    });

    // Observe Skill Categories (New)
    document.querySelectorAll('.skill-category').forEach(cat => {
        cat.style.opacity = '0';
        cat.style.transform = 'translateY(30px)';
        cat.style.transition = 'all 0.6s ease';
        animateOnScroll.observe(cat);
    });

    // Observe Timeline Items for Fade In
    document.querySelectorAll('.timeline-item').forEach(item => {
        item.style.opacity = '0';
        item.style.transform = 'translateY(30px)';
        item.style.transition = 'all 0.6s ease';
        animateOnScroll.observe(item);
    });

    // Observe Interest Cards
    document.querySelectorAll('.interest-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'all 0.6s ease';
        animateOnScroll.observe(card);
    });

    // Observe Project Cards
    document.querySelectorAll('.project-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'all 0.6s ease';
        animateOnScroll.observe(card);
    });


    // --- 5. Custom Cursor Glow ---
    const cursorGlow = document.createElement('div');
    cursorGlow.className = 'cursor-glow';
    document.body.appendChild(cursorGlow);

    window.addEventListener('mousemove', (e) => {
        cursorGlow.style.left = e.clientX + 'px';
        cursorGlow.style.top = e.clientY + 'px';
    });

    // --- 6. Vanilla Tilt Effect (Simple Version) ---
    const tiltElements = document.querySelectorAll('[data-tilt]');

    tiltElements.forEach(item => {
        item.addEventListener('mousemove', (e) => {
            const rect = item.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            // Calculate rotation (center is 0)
            const xPct = (x / rect.width) - 0.5;
            const yPct = (y / rect.height) - 0.5;

            // Limit rotation to 15deg
            const xRot = yPct * -15;
            const yRot = xPct * 15;

            item.querySelector('img').style.transform = `scale(1.05) perspective(1000px) rotateX(${xRot}deg) rotateY(${yRot}deg)`;
        });

        item.addEventListener('mouseleave', () => {
            item.querySelector('img').style.transform = `scale(1) perspective(1000px) rotateX(0) rotateY(0)`;
        });
    });

    // --- 7. Theme Toggle Logic ---
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = themeToggle.querySelector('i');
    const body = document.body;

    // Check for saved theme preference
    if (localStorage.getItem('theme') === 'light') {
        body.classList.add('light-mode');
        themeIcon.classList.replace('fa-moon', 'fa-sun');
    }

    themeToggle.addEventListener('click', () => {
        body.classList.toggle('light-mode');
        const isLight = body.classList.contains('light-mode');

        // Update persistent storage
        localStorage.setItem('theme', isLight ? 'light' : 'dark');

        // Update icon with animation
        if (isLight) {
            themeIcon.classList.replace('fa-moon', 'fa-sun');
        } else {
            themeIcon.classList.replace('fa-sun', 'fa-moon');
        }
    });

});
