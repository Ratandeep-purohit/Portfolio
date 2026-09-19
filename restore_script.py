import re
import os

filepath = 'index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Restore Hero Tagline
hero_old = """                    <p class="hero-tagline">
                        Specializing in <strong>high-performance systems</strong>, <strong>intelligent AI automation</strong>, 
                        and <strong>scalable full-stack architectures</strong>. I bridge the gap between complex 
                        backend engineering and premium digital experiences.
                    </p>"""
hero_new = """                    <p class="hero-tagline">
                        Specializing in <strong>high-performance systems</strong>, <strong>intelligent AI
                            automation</strong>,
                        and <strong>scalable full-stack architectures</strong>. I bridge the gap between complex
                        backend engineering and premium digital experiences.
                    </p>"""
content = content.replace(hero_old, hero_new)

# 2. Restore Bio Title
bio_title_old = """                        <h2 class="section-title">Engineering <span class="gradient-text">Intelligent</span> <br>Digital Solutions</h2>"""
bio_title_new = """                        <h2 class="section-title">Engineering <span class="gradient-text">Intelligent</span> <br>Digital
                            Solutions</h2>"""
content = content.replace(bio_title_old, bio_title_new)

# 3. Restore Bio Content
bio_old = """                        <div class="bio-content">
                            <p><strong>Ratandeep Purohit</strong> is a Software Engineer, AI Developer, and Full-Stack Technology Enthusiast from India, passionate about building scalable backend systems, intelligent AI-powered applications, and modern digital experiences. He specializes in <strong>Python, FastAPI, Django, Flask, Machine Learning, Generative AI, NLP,</strong> and cloud-ready architectures, with a strong focus on production-grade software engineering and real-world problem solving.</p>
                            
                            <p>Currently pursuing a <strong>Master of Computer Applications (MCA)</strong> at Silver Oak University, Ratandeep is known for working on advanced projects involving AI agents, multi-agent systems, intelligent automation, vector databases, enterprise platforms, and modern web technologies. His technical interests include Artificial Intelligence, Cognitive Computing, Federated Learning, System Design, Cloud Infrastructure, and scalable application development.</p>
                            
                            <p>Beyond academics, he actively builds real-world applications, explores emerging technologies, participates in hackathons, and continuously experiments with futuristic software systems. His work combines backend engineering, AI integration, modern UI/UX development, and scalable architecture to create impactful digital solutions.</p>
                        </div>"""

bio_new = """                        <div class="bio-content">
                            <p><strong>Ratandeep Purohit</strong> is a Software Engineer, Computer Scientist and AI/ML
                                Engineer from India, focused on building production-grade AI systems, scalable backend
                                architectures, and intelligent software products. His work spans Python, FastAPI,
                                Django, Flask, Machine Learning, Deep Learning, Generative AI, NLP, React, and
                                cloud-ready architectures, with an emphasis on turning complex technical ideas into
                                deployable real-world applications.</p>

                            <p>Currently pursuing a <strong>Master of Computer Applications (MCA)</strong> at Silver Oak
                                University, Ratandeep works on projects involving AI agents, multi-agent systems,
                                intelligent automation, enterprise SaaS platforms, cybersecurity, voice-cloning
                                detection, search systems, and modern full-stack applications. His technical interests
                                include Artificial Intelligence, Machine Learning, Deep Learning, System Design, Cloud
                                Infrastructure, and scalable software architecture.</p>

                            <p>Alongside his academic work, he actively develops and deploys software products,
                                participates in hackathons, and experiments with emerging AI technologies. His
                                engineering approach combines backend development, AI/ML integration, full-stack
                                development, system architecture, and production deployment to build software that moves
                                beyond prototypes and into working products.</p>
                        </div>"""
content = content.replace(bio_old, bio_new)

# 4. Restore Voice Cloning Project
proj_old = """                <div class="projects-grid">

                    <!-- Card 1: BURNOUT-X -->
                    <article class="project-card project-featured" data-aos="fade-up" data-aos-delay="0">"""

proj_new = """                <div class="projects-grid">

                    <!-- ── Featured: AI-Powered Voice Cloning Detection ── -->
                    <article class="project-card project-featured" data-aos="fade-up" data-aos-delay="0"
                        id="voice-cloning-detection-project">
                        <div class="project-img-wrap">
                            <img src="photos/voice-clone.jpg"
                                alt="AI-Powered Voice Cloning Detection & Prevention System — audio waveform analysis dashboard by Ratandeep Purohit"
                                loading="lazy">
                            <div class="project-category-tag">AI / Cybersecurity</div>
                        </div>
                        <div class="project-body">
                            <h3>AI-Powered Voice Cloning Detection &amp; Prevention System</h3>
                            <p>A production-deployed system for detecting AI-generated and cloned voices using
                                <strong>AASIST</strong> (Anti-Spoofing using Integrated Spectro-Temporal graph
                                attention networks) via PyTorch. Performs deterministic risk scoring, applies
                                configurable prevention policies, and triggers security alerts. Deployed on Render
                                (backend) and Vercel (frontend) with Supabase-backed audit logging.</p>
                            <div class="project-tags">
                                <span>PyTorch</span><span>AASIST</span><span>FastAPI</span><span>React</span><span>TypeScript</span><span>Supabase</span><span>Hugging Face</span><span>Vercel</span>
                            </div>
                            <div class="project-links-row">
                                <a href="https://github.com/Ratandeep-purohit/AI-Powered-Voice-Cloning-Detection-System"
                                    target="_blank" rel="noopener noreferrer" class="proj-link-btn"
                                    aria-label="View AI-Powered Voice Cloning Detection System source code on GitHub">
                                    <i class="fab fa-github"></i> Source Code
                                </a>
                                <a href="https://ai-powered-voice-cloning-detection.vercel.app" target="_blank"
                                    rel="noopener noreferrer" class="proj-link-btn proj-link-secondary"
                                    aria-label="Open AI-Powered Voice Cloning Detection live demo">
                                    <i class="fas fa-external-link-alt"></i> Live Demo
                                </a>
                            </div>
                        </div>
                    </article>

                    <!-- Card: BURNOUT-X -->
                    <article class="project-card" data-aos="fade-up" data-aos-delay="0">"""
content = content.replace(proj_old, proj_new)

content = content.replace("<!-- Card 2: Seekora -->", "<!-- Card: Seekora -->")
content = content.replace("<!-- Card 3: SentinelLite -->", "<!-- Card: SentinelLite -->")
content = content.replace("<!-- Card 4: Multi-Agent SalesOps Arena -->", "<!-- Card: Multi-Agent SalesOps Arena -->")


# 5. Restore Products Section
products_section = """
        <!-- ═══════════════════════ PRODUCTS SECTION ═══════════════════════ -->
        <section id="products" class="section products-section"
            aria-label="Software Products Built by Ratandeep Purohit">
            <div class="container">
                <div class="section-header" data-aos="fade-up">
                    <span class="section-badge">Live Products</span>
                    <h2 class="section-title">Products <span class="gradient-text">I've Built</span></h2>
                    <p class="section-subtitle">I build and deploy real-world software products, combining backend
                        engineering, SaaS architecture, AI/ML, and modern web technologies.</p>
                </div>

                <div class="products-grid">

                    <!-- ── Product 1: GlassEntials CRM ── -->
                    <article class="product-card" data-aos="fade-up" data-aos-delay="0">
                        <div class="product-screenshot-wrap">
                            <img src="photos/CRM.jpeg"
                                alt="GlassEntials CRM dashboard — glass industry business management software built by Ratandeep Purohit"
                                loading="lazy">
                            <div class="product-live-badge">
                                <span class="product-live-dot"></span>
                                Live Product
                            </div>
                            <div class="product-overlay-tag">CRM</div>
                        </div>
                        <div class="product-body">
                            <span class="product-type-tag">Python · Flask · SQLAlchemy · MySQL</span>
                            <h3>GlassEntials CRM</h3>
                            <p>A high-performance Customer Relationship Management platform built exclusively for the
                                glass and mirror industry. Manages the full client lifecycle — from lead capture to
                                project delivery — with a production-grade backend and a custom Glassmorphism UI.</p>
                            <ul class="product-features" aria-label="GlassEntials CRM key capabilities">
                                <li><i class="fas fa-circle-check"></i> Customer &amp; Lead Management</li>
                                <li><i class="fas fa-circle-check"></i> Project &amp; Task Tracking</li>
                                <li><i class="fas fa-circle-check"></i> Soft Delete Architecture</li>
                                <li><i class="fas fa-circle-check"></i> Internal Staff Portal</li>
                                <li><i class="fas fa-circle-check"></i> 30% Faster Turnaround</li>
                                <li><i class="fas fa-circle-check"></i> Real-time Assignment Logic</li>
                            </ul>
                            <div class="product-cta">
                                <a href="https://glassentials.in" target="_blank" rel="noopener noreferrer"
                                    class="btn-product" aria-label="Explore GlassEntials CRM live application">
                                    Explore Product <i class="fas fa-external-link-alt"></i>
                                </a>
                            </div>
                        </div>
                    </article>

                    <!-- ── Product 2: Mulzon HRMS ── -->
                    <article class="product-card" data-aos="fade-up" data-aos-delay="120">
                        <div class="product-screenshot-wrap">
                            <img src="photos/HRMS.jpeg"
                                alt="Mulzon HRMS dashboard — enterprise human resource management platform built by Ratandeep Purohit"
                                loading="lazy">
                            <div class="product-live-badge">
                                <span class="product-live-dot"></span>
                                Live Product
                            </div>
                            <div class="product-overlay-tag">HRMS</div>
                        </div>
                        <div class="product-body">
                            <span class="product-type-tag">Python · Django 5 · PostgreSQL</span>
                            <h3>Mulzon HRMS</h3>
                            <p>An enterprise-grade Human Resource Management System built on Django 5.x, designed to
                                automate workforce administration, attendance tracking, shift management, and the full
                                payroll lifecycle. Actively used by business teams for day-to-day HR operations.</p>
                            <ul class="product-features" aria-label="Mulzon HRMS key capabilities">
                                <li><i class="fas fa-circle-check"></i> Employee Lifecycle Management</li>
                                <li><i class="fas fa-circle-check"></i> Attendance &amp; Shift Tracking</li>
                                <li><i class="fas fa-circle-check"></i> Automated Payroll Systems</li>
                                <li><i class="fas fa-circle-check"></i> Leave Management Portal</li>
                                <li><i class="fas fa-circle-check"></i> Department &amp; Role RBAC</li>
                                <li><i class="fas fa-circle-check"></i> Comprehensive Reporting</li>
                            </ul>
                            <div class="product-cta">
                                <a href="https://hrms.mulzon.tech" target="_blank" rel="noopener noreferrer"
                                    class="btn-product" aria-label="Explore Mulzon HRMS live application">
                                    Explore Product <i class="fas fa-external-link-alt"></i>
                                </a>
                            </div>
                        </div>
                    </article>

                </div>
            </div>
        </section>
"""

# Insert products before CTA Banner
cta_marker = "<!-- ═══════════════════════ CTA BANNER ═══════════════════════ -->"
content = content.replace(cta_marker, products_section + "\n\n        " + cta_marker)


# 6. Restore Footer structure that was in git diff
footer_old = """    <footer class="footer" aria-label="Site Footer">
        <div class="container">
            <div class="footer-top">
                <div class="footer-brand">
                    <div class="logo">RP<span class="dot">.</span></div>
                    <p>Software Engineer & AI Developer<br>based in Ahmedabad, India.</p>
                </div>
                <div class="footer-nav-col">
                    <h4>Pages</h4>
                    <ul>
                        <li><a href="about.html">About</a></li>
                        <li><a href="skills.html">Skills</a></li>
                        <li><a href="projects.html">Projects</a></li>
                        <li><a href="experience.html">Experience</a></li>
                        <li><a href="achievements.html">Achievements and Certificates</a></li>
                    </ul>
                </div>
                <div class="footer-nav-col">
                    <h4>Contact</h4>
                    <ul>
                        <li><a href="mailto:Rajatpurohit183@gmail.com"><i class="fas fa-envelope"></i> Email</a></li>
                        <li><a href="https://github.com/Ratandeep-purohit" target="_blank"><i class="fab fa-github"></i>
                                GitHub</a></li>
                        <li><a href="https://www.linkedin.com/in/ratandeep-purohit-ab0309304/" target="_blank"><i
                                    class="fab fa-linkedin-in"></i> LinkedIn</a></li>
                        <li><a href="resume.pdf" download><i class="fas fa-file-pdf"></i> Resume</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; <span id="current-year"></span> Ratandeep Purohit. All rights reserved.</p>
                <div class="footer-bottom-links">
                    <a href="sitemap.xml">Sitemap</a>
                    <a href="contact.html">Hire Me</a>
                </div>
            </div>
        </div>
    </footer>

    <script src="script.js?v=4.0" defer></script>
</body>

</html>"""

footer_new = """    <footer class="footer" aria-label="Site Footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-logo">RP<span class="dot">.</span></div>
                <div class="footer-socials">
                    <a href="https://github.com/Ratandeep-purohit" target="_blank" aria-label="GitHub"><i class="fab fa-github"></i></a>
                    <a href="https://www.linkedin.com/in/ratandeep-purohit-ab0309304/" target="_blank" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                    <a href="mailto:Rajatpurohit183@gmail.com" aria-label="Email"><i class="fas fa-envelope"></i></a>
                </div>
                <div class="footer-links">
                    <a href="sitemap.xml">Sitemap</a> | <a href="resume.pdf" target="_blank">Resume</a>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; <span id="current-year"></span> Ratandeep Purohit. All rights reserved.</p>
                <p>Designed & Built with <i class="fas fa-heart highlight-text"></i></p>
            </div>
        </div>
    </footer>
    <script src="script.js" defer></script>
</body>
</html>"""

content = content.replace(footer_old, footer_new)


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Restoration complete.")
