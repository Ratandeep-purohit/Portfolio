import os

BASE_URL = "https://ratandeep-purohit.github.io/Portfolio"

def get_header(title, description, canonical_path, og_image="burnout-x.png", schema_json=""):
    canonical_url = f"{BASE_URL}{canonical_path}"
    og_image_url = f"{BASE_URL}/{og_image}"
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    
    <title>{title}</title>
    <meta name="title" content="{title}">
    <meta name="description" content="{description}">
    <meta name="keywords" content="Ratandeep Purohit, Software Engineer, AI Developer, Python, Machine Learning, React, FastAPI, Django">
    <meta name="author" content="Ratandeep Purohit">
    <link rel="canonical" href="{canonical_url}">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="{og_image_url}">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="{canonical_url}">
    <meta property="twitter:title" content="{title}">
    <meta property="twitter:description" content="{description}">
    <meta property="twitter:image" content="{og_image_url}">

    <!-- Fonts & Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@300;400;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" media="print" onload="this.media='all'">

    <!-- Main Stylesheet -->
    <link rel="stylesheet" href="style.css?v=3.0">
    
    {schema_json}
</head>
<body>
    <button class="theme-toggle" id="theme-toggle" aria-label="Toggle Dark/Light Mode">
        <i class="fas fa-moon"></i>
    </button>

    <header class="header">
        <nav class="navbar container">
            <a href="index.html" class="logo" aria-label="Ratandeep Purohit Logo">RP<span class="dot">.</span></a>
            <ul class="nav-links">
                <li><a href="index.html" data-page="home">Home</a></li>
                <li><a href="about.html" data-page="about">About</a></li>
                <li><a href="skills.html" data-page="skills">Skills</a></li>
                <li><a href="projects.html" data-page="projects">Projects</a></li>
                <li><a href="experience.html" data-page="experience">Experience</a></li>
                <li><a href="achievements.html" data-page="achievements">Achievements</a></li>
                <li><a href="contact.html" class="btn-contact" data-page="contact">Hire Me</a></li>
            </ul>
            <div class="hamburger" aria-label="Toggle Menu">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </div>
        </nav>
    </header>
    <main>
'''

def get_footer():
    return f'''
    </main>
    <footer class="footer">
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
</html>
'''

# 1. index.html
schema_home = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Ratandeep Purohit",
  "jobTitle": "Software Engineer & AI Developer",
  "url": "https://ratandeep-purohit.github.io/Portfolio/",
  "sameAs": [
    "https://www.linkedin.com/in/ratandeep-purohit-ab0309304/",
    "https://github.com/Ratandeep-purohit"
  ]
}
</script>'''

content_home = '''
<section id="home" class="hero">
    <div class="container hero-container">
        <div class="hero-content">
            <span class="greeting">Hello, World! I am</span>
            <h1 class="name">Ratandeep Purohit</h1>
            <h2 class="role">I build <span class="typing-text"></span></h2>
            <p class="tagline">I engineer high-performance software systems and AI solutions. Specializing in Python, React, and scalable backend architectures.</p>
            <div class="hero-btns">
                <a href="projects.html" class="btn btn-primary">Explore My Work</a>
                <a href="resume.pdf" class="btn btn-secondary" download><i class="fas fa-file-download"></i> Download Resume</a>
            </div>
        </div>
        <div class="hero-visual">
            <div class="profile-frame">
                <div class="glow-ring"></div>
                <img src="pic.jpg" alt="Ratandeep Purohit" class="profile-pic" onerror="this.src='https://images.unsplash.com/photo-1549692520-acc6669e2f0c?q=80&w=800&auto=format&fit=crop'">
                
                <!-- Floating Tech Badges -->
                <div class="floating-badge badge-1" title="Python Expert">
                    <i class="fab fa-python"></i>
                </div>
                <div class="floating-badge badge-2" title="AI Developer">
                    <i class="fas fa-brain"></i>
                </div>
                <div class="floating-badge badge-3" title="Full Stack">
                    <i class="fas fa-layer-group"></i>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="section bg-alt">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title">Featured <span class="highlight">Projects</span></h2>
            <p class="section-subtitle">A glimpse of my best work</p>
        </div>
        <div class="projects-grid">
            <article class="project-card">
                <div class="project-image">
                    <img src="burnout-x.png" alt="BURNOUT-X AI Dashboard" loading="lazy">
                    <div class="project-links">
                        <a href="https://github.com/Ratandeep-purohit/AETHER" target="_blank" aria-label="View Source"><i class="fab fa-github"></i></a>
                    </div>
                </div>
                <div class="project-info">
                    <h3 class="project-title">BURNOUT-X <span class="badge badge-primary">AI</span></h3>
                    <p class="project-desc">Enterprise AI system predicting employee burnout risk 4 weeks early using multi-modal signal processing (XGBoost + SHAP).</p>
                    <div class="tech-tags">
                        <span>Python</span><span>FastAPI</span><span>React</span><span>XGBoost</span>
                    </div>
                </div>
            </article>
            <article class="project-card">
                <div class="project-image">
                    <img src="https://images.unsplash.com/photo-1550439062-609e1531270e?q=80&w=800&auto=format&fit=crop" alt="Seekora Search Engine" loading="lazy">
                    <div class="project-links">
                        <a href="https://github.com/Ratandeep-purohit/Seekora" target="_blank" aria-label="View Source"><i class="fab fa-github"></i></a>
                    </div>
                </div>
                <div class="project-info">
                    <h3 class="project-title">Seekora Search Engine <span class="badge badge-secondary">Full Stack</span></h3>
                    <p class="project-desc">Distributed search engine with custom crawler, Lucene-based inverted indexer, and hybrid ranking.</p>
                    <div class="tech-tags">
                        <span>Django</span><span>React</span><span>MySQL</span>
                    </div>
                </div>
            </article>
        </div>
        <div style="text-align: center; margin-top: 40px;">
            <a href="projects.html" class="btn btn-secondary">View All Projects</a>
        </div>
    </div>
</section>
'''

# 2. about.html
schema_about = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [{
    "@type": "ListItem", "position": 1, "name": "Home", "item": "https://ratandeep-purohit.github.io/Portfolio/"
  },{
    "@type": "ListItem", "position": 2, "name": "About Me", "item": "https://ratandeep-purohit.github.io/Portfolio/about.html"
  }]
}
</script>'''

content_about = '''
<section class="section" style="padding-top: 150px;">
    <div class="container">
        <div class="section-header">
            <h1 class="section-title">About <span class="highlight">Me</span></h1>
            <p class="section-subtitle">Bridging the gap between Complex Logic and Elegant Design</p>
        </div>
        
        <div class="about-grid">
            <div class="about-image-wrapper" data-tilt>
                <img src="https://images.unsplash.com/photo-1549692520-acc6669e2f0c?q=80&w=800&auto=format&fit=crop" alt="Ratandeep Purohit - Software Engineer Coding" loading="lazy" class="about-img">
                <div class="experience-badge">
                    <span class="years">2+</span>
                    <span class="text">Years<br>Coding</span>
                </div>
            </div>
            <div class="about-content">
                <h3>Software Engineer | AI Developer | Lifelong Learner</h3>
                <p>I am a passionate <strong>Software Engineer</strong> and <strong>MCA Student</strong> based in Ahmedabad. I specialize in building robust, scalable web applications and integrating cutting-edge <strong>Artificial Intelligence</strong> to solve real-world problems.</p>
                <p>My journey began with a BCA from Shree Jain PG College, where I built strong foundations in Data Structures, Algorithms, and Object-Oriented Programming (graduating with a 7.72 CGPA). Currently, I am pursuing my Master of Computer Applications (MCA) at Silver Oak University, specializing in advanced software engineering, system architecture, and AI.</p>
                <p>My expertise lies in backend architecture (Python, FastAPI, Django) combined with modern frontend frameworks (React, Tailwind). I thrive in environments that challenge me to optimize performance and engineer seamless user experiences.</p>
                <p>Beyond coding, I have a deep interest in Generative AI, Cyber Security, and Space Science. My career goal is to engineer intelligent systems that impact millions of users globally.</p>
                
                <div class="metrics-grid">
                    <div class="metric-card">
                        <h4 class="metric-number">10+</h4>
                        <p class="metric-label">Projects Built</p>
                    </div>
                    <div class="metric-card">
                        <h4 class="metric-number">3+</h4>
                        <p class="metric-label">Hackathons</p>
                    </div>
                    <div class="metric-card">
                        <h4 class="metric-number">5K+</h4>
                        <p class="metric-label">Lines of Code</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
'''

# 3. skills.html
content_skills = '''
<section class="section bg-alt" style="padding-top: 150px;">
    <div class="container">
        <div class="section-header">
            <h1 class="section-title">Technical <span class="highlight">Arsenal</span></h1>
            <p class="section-subtitle">Categorized breakdown of my technical capabilities</p>
        </div>

        <div class="skills-grid">
            <div class="skill-card">
                <div class="skill-icon"><i class="fas fa-code"></i></div>
                <h3>Programming Languages</h3>
                <ul class="skill-list">
                    <li><i class="fab fa-python"></i> Python (Advanced)</li>
                    <li><i class="fab fa-java"></i> Java</li>
                    <li><i class="fab fa-js"></i> JavaScript / TypeScript</li>
                    <li><i class="fas fa-terminal"></i> C++ / PHP</li>
                </ul>
            </div>

            <div class="skill-card">
                <div class="skill-icon"><i class="fas fa-server"></i></div>
                <h3>Backend Development</h3>
                <ul class="skill-list">
                    <li><i class="fas fa-bolt"></i> FastAPI</li>
                    <li><i class="fas fa-leaf"></i> Django</li>
                    <li><i class="fas fa-pepper-hot"></i> Flask</li>
                    <li><i class="fab fa-node-js"></i> Node.js (Express)</li>
                </ul>
            </div>

            <div class="skill-card">
                <div class="skill-icon"><i class="fas fa-laptop-code"></i></div>
                <h3>Frontend Development</h3>
                <ul class="skill-list">
                    <li><i class="fab fa-react"></i> React.js</li>
                    <li><i class="fab fa-html5"></i> HTML5 & CSS3</li>
                    <li><i class="fab fa-css3-alt"></i> Tailwind CSS</li>
                    <li><i class="fas fa-layer-group"></i> Material UI</li>
                </ul>
            </div>

            <div class="skill-card">
                <div class="skill-icon"><i class="fas fa-brain"></i></div>
                <h3>AI / ML & Gen AI</h3>
                <ul class="skill-list">
                    <li><i class="fas fa-robot"></i> NLP / Computer Vision</li>
                    <li><i class="fas fa-project-diagram"></i> LangChain / LangGraph</li>
                    <li><i class="fas fa-chart-network"></i> Scikit-learn / XGBoost</li>
                    <li><i class="fas fa-eye"></i> OpenCV</li>
                    <li><i class="fas fa-brain"></i> Hugging Face</li>
                </ul>
            </div>

            <div class="skill-card">
                <div class="skill-icon"><i class="fas fa-database"></i></div>
                <h3>Databases</h3>
                <ul class="skill-list">
                    <li><i class="fas fa-database"></i> MySQL</li>
                    <li><i class="fas fa-leaf"></i> MongoDB</li>
                    <li><i class="fas fa-server"></i> PostgreSQL</li>
                    <li><i class="fas fa-search"></i> Qdrant (Vector DB)</li>
                    <li><i class="fas fa-memory"></i> Redis</li>
                </ul>
            </div>

            <div class="skill-card">
                <div class="skill-icon"><i class="fas fa-cloud"></i></div>
                <h3>DevOps, Cloud & Tools</h3>
                <ul class="skill-list">
                    <li><i class="fab fa-docker"></i> Docker</li>
                    <li><i class="fab fa-aws"></i> AWS (EC2, S3)</li>
                    <li><i class="fab fa-git-alt"></i> Git / GitHub</li>
                    <li><i class="fas fa-network-wired"></i> REST APIs</li>
                    <li><i class="fas fa-terminal"></i> Linux / Bash</li>
                </ul>
            </div>
        </div>
    </div>
</section>
'''

# 4. projects.html
content_projects = '''
<section class="section" style="padding-top: 150px;">
    <div class="container">
        <div class="section-header">
            <h1 class="section-title">Dedicated <span class="highlight">Projects</span> Showcase</h1>
            <p class="section-subtitle">In-depth case studies of my software engineering work</p>
        </div>

        <div class="project-filters">
            <button class="filter-btn active" data-filter="all">All</button>
            <button class="filter-btn" data-filter="fullstack">Full Stack</button>
            <button class="filter-btn" data-filter="ai">AI / ML</button>
            <button class="filter-btn" data-filter="backend">Backend</button>
        </div>

        <div class="projects-grid">
            <!-- Project 1 -->
            <article class="project-card" data-category="ai fullstack">
                <div class="project-image">
                    <img src="burnout-x.png" alt="BURNOUT-X AI Dashboard" loading="lazy">
                    <div class="project-links">
                        <a href="https://github.com/Ratandeep-purohit/AETHER" target="_blank" rel="noopener noreferrer"><i class="fab fa-github"></i></a>
                    </div>
                </div>
                <div class="project-info">
                    <h3 class="project-title">BURNOUT-X <span class="badge badge-primary">AI</span></h3>
                    <p class="project-desc"><strong>Problem Solved:</strong> High employee turnover due to undetected burnout.<br><br>Enterprise AI system predicting employee burnout risk 4 weeks early using multi-modal signal processing (XGBoost + SHAP). Features a high-performance React dashboard.</p>
                    <div class="tech-tags">
                        <span>Python</span><span>FastAPI</span><span>React</span><span>XGBoost</span><span>Tailwind</span>
                    </div>
                </div>
            </article>

            <!-- Project 2 -->
            <article class="project-card" data-category="fullstack backend">
                <div class="project-image">
                    <img src="https://images.unsplash.com/photo-1550439062-609e1531270e?q=80&w=800&auto=format&fit=crop" alt="Seekora Search Engine" loading="lazy">
                    <div class="project-links">
                        <a href="https://github.com/Ratandeep-purohit/Seekora" target="_blank" rel="noopener noreferrer"><i class="fab fa-github"></i></a>
                    </div>
                </div>
                <div class="project-info">
                    <h3 class="project-title">Seekora Search Engine <span class="badge badge-secondary">Full Stack</span></h3>
                    <p class="project-desc"><strong>Problem Solved:</strong> Need for an internal, distributed indexing solution.<br><br>Industry-standard distributed search engine with a custom crawler, Lucene-based inverted indexer, and hybrid ranking system.</p>
                    <div class="tech-tags">
                        <span>Django</span><span>React</span><span>TypeScript</span><span>MySQL</span>
                    </div>
                </div>
            </article>

            <!-- Project 3 -->
            <article class="project-card" data-category="backend ai">
                <div class="project-image">
                    <img src="https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=800&auto=format&fit=crop" alt="SentinelLite Cybersecurity" loading="lazy">
                    <div class="project-links">
                        <a href="https://github.com/TitanGuard-Labs/SentinelLite" target="_blank" rel="noopener noreferrer"><i class="fab fa-github"></i></a>
                    </div>
                </div>
                <div class="project-info">
                    <h3 class="project-title">SentinelLite <span class="badge badge-accent">Cybersec</span></h3>
                    <p class="project-desc"><strong>Problem Solved:</strong> Lightweight heuristic malware detection for legacy systems.<br><br>Professional-grade cybersecurity tool featuring a heuristic malware detection engine, real-time threat telemetry charts, and a quarantine vault.</p>
                    <div class="tech-tags">
                        <span>Python</span><span>PyQt5</span><span>SQLite</span><span>Matplotlib</span>
                    </div>
                </div>
            </article>

            <!-- Project 4 -->
            <article class="project-card" data-category="fullstack">
                <div class="project-image">
                    <img src="https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?q=80&w=800&auto=format&fit=crop" alt="DigiTechHealth Hospital Management" loading="lazy">
                    <div class="project-links">
                        <a href="https://github.com/Ratandeep-purohit/DigiTechHealth" target="_blank" rel="noopener noreferrer"><i class="fab fa-github"></i></a>
                    </div>
                </div>
                <div class="project-info">
                    <h3 class="project-title">DigiTechHealth <span class="badge badge-secondary">Full Stack</span></h3>
                    <p class="project-desc"><strong>Problem Solved:</strong> Fragmented hospital operations and patient record keeping.<br><br>End-to-end Hospital Operations Platform streamlining workflows with RBAC, secure auth, and a premium glassmorphic UI.</p>
                    <div class="tech-tags">
                        <span>Flask</span><span>SQLAlchemy</span><span>Tailwind</span><span>SQLite</span>
                    </div>
                </div>
            </article>
            
            <!-- Project 5 -->
            <article class="project-card" data-category="backend">
                <div class="project-image">
                    <img src="https://images.unsplash.com/photo-1587854692152-cbe660dbde88?q=80&w=800&auto=format&fit=crop" alt="Pharmacy API" loading="lazy">
                    <div class="project-links">
                        <a href="https://github.com/Ratandeep-purohit/Pharmacy-Management-System-REST-API-" target="_blank" rel="noopener noreferrer"><i class="fab fa-github"></i></a>
                    </div>
                </div>
                <div class="project-info">
                    <h3 class="project-title">Pharmacy Management API <span class="badge badge-primary">Backend</span></h3>
                    <p class="project-desc"><strong>Problem Solved:</strong> Secure, scalable inventory management for pharmacies.<br><br>Production-ready RESTful API implementing Clean Architecture, JWT Authentication, Marshmallow validation, and Role-Based Access Control.</p>
                    <div class="tech-tags">
                        <span>Flask REST API</span><span>JWT Auth</span><span>MySQL</span><span>Docker</span>
                    </div>
                </div>
            </article>
        </div>
    </div>
</section>
'''

# 5. experience.html
content_experience = '''
<section class="section bg-alt" style="padding-top: 150px;">
    <div class="container">
        <div class="section-header">
            <h1 class="section-title">Work <span class="highlight">Experience</span> & Journey</h1>
            <p class="section-subtitle">My professional and academic pathway</p>
        </div>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-content">
                    <span class="timeline-date">2025 - Present (2027)</span>
                    <h3>Master of Computer Applications (MCA)</h3>
                    <h4>Silver Oak University, Ahmedabad</h4>
                    <p>Pursuing advanced studies specializing in software architecture, system design, and artificial intelligence. Currently involved in extensive research and development projects.</p>
                </div>
            </div>
            
            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-content">
                    <span class="timeline-date">Nov 2025</span>
                    <h3>Advanced Certification: Python & Networking</h3>
                    <h4>Scaler Topics</h4>
                    <p>Mastered advanced Python development, asynchronous programming, and deep-dived into core Networking protocols (OSI, TCP/IP, HTTP/REST).</p>
                </div>
            </div>

            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-content">
                    <span class="timeline-date">2022 - 2025</span>
                    <h3>Bachelor of Computer Applications (BCA)</h3>
                    <h4>Shree Jain PG College</h4>
                    <p>Graduated with 7.72 CGPA. Built strong foundations in Data Structures, Algorithms, Database Management Systems, and Object-Oriented Programming.</p>
                </div>
            </div>
            
            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-content">
                    <span class="timeline-date">Ongoing</span>
                    <h3>Independent Software Developer & Researcher</h3>
                    <h4>Freelance & Open Source</h4>
                    <p>Developing robust, scalable web applications and exploring the frontiers of AI. Conducting independent research in computer science and contributing to community-driven software.</p>
                </div>
            </div>
        </div>
    </div>
</section>
'''

# 6. achievements.html
content_achievements = '''
<section class="section" style="padding-top: 150px;">
    <div class="container">
        <div class="section-header">
            <h1 class="section-title">Awards & <span class="highlight">Achievements</span></h1>
            <p class="section-subtitle">Hackathons, certifications, and public recognition</p>
        </div>

        <div class="projects-grid">
            <div class="glass-card" style="padding: 30px;">
                <div class="icon-box" style="margin-bottom: 20px;"><i class="fas fa-trophy"></i></div>
                <h3>Hackathons</h3>
                <p style="color: var(--text-muted); margin-top: 10px;">Participated in 3+ major hackathons, leading teams to build innovative AI-driven and Full Stack solutions under tight deadlines. Developed prototypes focusing on social impact and enterprise efficiency.</p>
            </div>
            
            <div class="glass-card" style="padding: 30px;">
                <div class="icon-box" style="margin-bottom: 20px;"><i class="fas fa-certificate"></i></div>
                <h3>Certifications</h3>
                <p style="color: var(--text-muted); margin-top: 10px;">Earned 2+ professional certifications including Advanced Python & Networking from Scaler Topics, validating expertise in core programming constructs and network architecture.</p>
            </div>
            
            <div class="glass-card" style="padding: 30px;">
                <div class="icon-box" style="margin-bottom: 20px;"><i class="fab fa-github"></i></div>
                <h3>Open Source & GitHub</h3>
                <p style="color: var(--text-muted); margin-top: 10px;">Active contributor to the open-source community with numerous repositories demonstrating clean architecture, production-ready APIs, and complex AI integrations.</p>
            </div>
        </div>
    </div>
</section>
'''

# 7. contact.html
content_contact = '''
<section class="section bg-alt" style="padding-top: 150px;">
    <div class="container">
        <div class="contact-wrapper">
            <div class="contact-info">
                <h1 class="section-title">Let's <span class="highlight">Connect</span></h1>
                <p class="contact-desc">I am currently open for Software Engineer, AI Developer, and Full Stack roles. Whether you have a project in mind, a role to fill, or just want to chat about technology, feel free to reach out!</p>
                
                <div class="contact-methods">
                    <a href="mailto:Rajatpurohit183@gmail.com" class="contact-method">
                        <div class="icon-box"><i class="fas fa-envelope"></i></div>
                        <div>
                            <h4>Email</h4>
                            <span>Rajatpurohit183@gmail.com</span>
                        </div>
                    </a>
                    <a href="https://www.linkedin.com/in/ratandeep-purohit-ab0309304/" target="_blank" rel="noopener noreferrer" class="contact-method">
                        <div class="icon-box"><i class="fab fa-linkedin-in"></i></div>
                        <div>
                            <h4>LinkedIn</h4>
                            <span>Connect Professionally</span>
                        </div>
                    </a>
                    <a href="https://github.com/Ratandeep-purohit" target="_blank" rel="noopener noreferrer" class="contact-method">
                        <div class="icon-box"><i class="fab fa-github"></i></div>
                        <div>
                            <h4>GitHub</h4>
                            <span>View My Code</span>
                        </div>
                    </a>
                </div>
            </div>
            
            <div class="contact-form-container">
                <div class="glass-card cta-card">
                    <h3>Ready to build something amazing?</h3>
                    <p>Download my resume to see my full professional background, complete skill set, and academic achievements.</p>
                    <a href="resume.pdf" class="btn btn-primary btn-large" download style="margin-top: 20px;"><i class="fas fa-download"></i> Get My Resume</a>
                </div>
            </div>
        </div>
    </div>
</section>
'''

# 8. 404.html
content_404 = '''
<section class="section" style="padding-top: 150px; text-align: center; min-height: 80vh; display: flex; flex-direction: column; justify-content: center; align-items: center;">
    <div class="container">
        <h1 class="section-title" style="font-size: 6rem; margin-bottom: 10px;"><span class="highlight">404</span></h1>
        <h2 style="font-size: 2rem; margin-bottom: 20px;">Page Not Found</h2>
        <p style="color: var(--text-muted); margin-bottom: 40px; max-width: 500px; margin-left: auto; margin-right: auto;">The page you are looking for might have been removed, had its name changed, or is temporarily unavailable.</p>
        <a href="index.html" class="btn btn-primary"><i class="fas fa-home"></i> Return to Home</a>
    </div>
</section>
'''

pages = [
    ("index.html", "Ratandeep Purohit | Software Engineer & AI Developer", "Portfolio of Ratandeep Purohit - Software Engineer specializing in Python, AI/ML, FastAPI, Django, and modern web applications.", "/", content_home, schema_home),
    ("about.html", "About Ratandeep Purohit | Software Engineer", "Learn about Ratandeep Purohit's background, education (MCA/BCA), and passion for AI and Software Engineering.", "/about.html", content_about, schema_about),
    ("skills.html", "Technical Skills | Ratandeep Purohit", "Explore the technical skills, programming languages, backend frameworks, and AI tools used by Ratandeep Purohit.", "/skills.html", content_skills, ""),
    ("projects.html", "Projects Portfolio | Ratandeep Purohit", "View case studies and technical details of projects built by Ratandeep Purohit including BURNOUT-X and Seekora.", "/projects.html", content_projects, ""),
    ("experience.html", "Experience & Journey | Ratandeep Purohit", "Detailed timeline of Ratandeep Purohit's academic journey, certifications, and software development experience.", "/experience.html", content_experience, ""),
    ("achievements.html", "Achievements & Awards | Ratandeep Purohit", "Hackathons, certifications, and open source contributions by Ratandeep Purohit.", "/achievements.html", content_achievements, ""),
    ("contact.html", "Contact Ratandeep Purohit | Hire Me", "Get in touch with Ratandeep Purohit for Software Engineering and AI Developer roles.", "/contact.html", content_contact, ""),
    ("404.html", "Page Not Found | Ratandeep Purohit", "The requested page could not be found.", "/404.html", content_404, ""),
]

for filename, title, desc, path, content, schema in pages:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(get_header(title, desc, path, schema_json=schema))
        f.write(content)
        f.write(get_footer())

print("HTML pages generated successfully.")
