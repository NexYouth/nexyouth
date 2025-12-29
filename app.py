from flask import Flask, render_template, render_template_string, send_from_directory, request
import os

app = Flask(__name__, static_folder='static', static_url_path='/static', template_folder='templates')

@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serve static files from static folder"""
    return send_from_directory(os.path.join(os.path.dirname(__file__), 'static'), filename)

# ============== HOME PAGE ==============
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="NexYouth - Empowering youth globally through skill development and mentorship.">
    <title>NexYouth - Empowering Youth</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #fff;
        }

        /* Navigation */
        nav {
            background: white;
            border-bottom: 1px solid #eee;
            position: sticky;
            top: 0;
            z-index: 50;
            padding: 0.8rem 2rem;
        }

        nav .container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        nav .logo {
            display: flex;
            align-items: center;
            text-decoration: none;
        }

        nav .logo img {
            height: 70px;
            width: auto;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        nav li {
            position: relative;
        }

        nav a {
            text-decoration: none;
            color: #333;
            font-size: 1rem;
            font-weight: 500;
            transition: color 0.2s;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        nav a:hover {
            color: #00d4ff;
        }

        /* Dropdown Menu */
        .dropdown-menu {
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            min-width: 220px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            padding: 0.5rem 0;
            z-index: 100;
        }

        .dropdown:hover .dropdown-menu {
            display: block;
        }

        .dropdown-menu a {
            display: block;
            padding: 0.8rem 1.2rem;
            font-size: 0.9rem;
            text-transform: none;
            letter-spacing: 0;
        }

        .dropdown-menu a:hover {
            background: #f5f5f5;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        /* Hero Section */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-align: center;
            padding: 4rem 2rem;
            position: relative;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.5);
            z-index: 1;
        }

        .hero video {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: 0;
        }

        .hero .content {
            position: relative;
            z-index: 2;
            max-width: 800px;
        }

        .hero h1 {
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            line-height: 1.2;
        }

        .hero p {
            font-size: 1.3rem;
            margin-bottom: 2.5rem;
            opacity: 0.95;
        }

        .cta-button {
            display: inline-block;
            background: #ff6b35;
            color: white;
            padding: 0.9rem 2.5rem;
            border-radius: 4px;
            text-decoration: none;
            transition: background 0.3s ease;
            font-weight: 600;
            font-size: 1rem;
        }

        .cta-button:hover {
            background: #ff5520;
        }

        /* Section Styling */
        section {
            padding: 5rem 2rem;
        }

        section h2 {
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 3rem;
            text-align: center;
        }

        /* What We Do Section */
        .what-we-do {
            background: #f9f9f9;
        }

        .what-we-do p {
            font-size: 1.1rem;
            line-height: 1.8;
            max-width: 700px;
            margin: 0 auto 2rem;
            text-align: center;
            color: #666;
        }

        .action-links {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 2rem;
            flex-wrap: wrap;
        }

        .action-links a {
            color: #ff6b35;
            text-decoration: none;
            font-weight: 600;
            transition: color 0.2s;
        }

        .action-links a:hover {
            color: #ff5520;
        }

        /* Programs Grid */
        .programs-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1rem;
        }

        .program-card {
            background: white;
            border: 1px solid #eee;
            padding: 2.5rem;
            border-radius: 4px;
            transition: all 0.3s ease;
            display: block;
            cursor: pointer;
        }

        .program-card:hover {
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
            transform: translateY(-4px);
            border-color: #00d4ff;
        }

        .program-card h3 {
            font-size: 1.3rem;
            margin-bottom: 1rem;
            font-weight: 700;
            transition: color 0.3s ease;
        }

        .program-card:hover h3 {
            color: #00d4ff;
        }

        .program-card p {
            color: #666;
            line-height: 1.7;
        }

        /* Statistics Section */
        .statistics {
            background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #0d2137 100%);
            color: white;
            padding: 6rem 2rem;
            position: relative;
            overflow: hidden;
        }

        .statistics::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 20% 50%, rgba(0, 212, 255, 0.1) 0%, transparent 50%),
                        radial-gradient(circle at 80% 50%, rgba(255, 107, 53, 0.1) 0%, transparent 50%);
            pointer-events: none;
        }

        .statistics h2 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: white;
            position: relative;
        }

        .statistics > .container > p {
            text-align: center;
            color: rgba(255, 255, 255, 0.7);
            font-size: 1.1rem;
            margin-bottom: 3rem;
            position: relative;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(6, 1fr);
            gap: 1.5rem;
            max-width: 1200px;
            margin: 0 auto;
            position: relative;
        }

        .stat-card {
            text-align: center;
            padding: 2rem 1rem;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: transform 0.3s, background 0.3s;
        }

        .stat-card:hover {
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.1);
        }

        .stat-number {
            font-size: 2.8rem;
            font-weight: 800;
            background: linear-gradient(135deg, #00d4ff 0%, #00a8cc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
        }

        @media (max-width: 1024px) {
            .stats-grid {
                grid-template-columns: repeat(3, 1fr);
            }
        }

        @media (max-width: 600px) {
            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        .stat-label {
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: white;
        }

        .stat-description {
            font-size: 0.9rem;
            opacity: 0.8;
            color: #ccc;
        }

        /* Testimonials Section */
        .testimonials {
            background: #f9f9f9;
        }

        .testimonials-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 2.5rem;
        }

        .testimonial-card {
            background: white;
            padding: 2rem;
            border-radius: 4px;
            border-left: 4px solid #ff6b35;
        }

        .testimonial-quote {
            font-style: italic;
            margin-bottom: 1.5rem;
            color: #666;
            line-height: 1.8;
        }

        .testimonial-author {
            font-weight: 700;
            margin-bottom: 0.3rem;
        }

        .testimonial-title {
            font-size: 0.9rem;
            color: #999;
        }

        /* CTA Section */
        .cta-section {
            background: #000;
            color: white;
            text-align: center;
            padding: 4rem 2rem;
        }

        .cta-section h2 {
            color: white;
            margin-bottom: 2rem;
        }

        /* Footer */
        footer {
            background: #000;
            color: white;
            padding: 3rem 2rem;
            text-align: center;
            border-top: 1px solid #333;
        }

        footer .links {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }

        footer a {
            color: #fff;
            text-decoration: none;
            font-size: 0.95rem;
            transition: color 0.2s;
        }

        footer a:hover {
            color: #ff6b35;
        }

        footer p {
            color: #999;
            font-size: 0.9rem;
        }

        @media (max-width: 768px) {
            nav {
                padding: 0.8rem 1rem;
            }

            nav .logo img {
                height: 50px;
            }

            nav ul {
                display: none;
                flex-direction: column;
                position: absolute;
                top: 100%;
                left: 0;
                right: 0;
                background: white;
                gap: 0;
                border-top: 1px solid #eee;
            }

            nav ul.active {
                display: flex;
            }

            nav li {
                width: 100%;
                position: relative;
            }

            nav a {
                display: block;
                padding: 1rem 2rem;
                font-size: 0.9rem;
                text-transform: uppercase;
            }

            .dropdown-menu {
                position: static;
                display: none;
                box-shadow: none;
                background: #f5f5f5;
                border-radius: 0;
                min-width: auto;
            }

            .dropdown-menu.active {
                display: block;
            }

            .dropdown-menu a {
                padding: 0.6rem 2rem 0.6rem 3rem;
                font-size: 0.85rem;
            }

            .dropdown:hover .dropdown-menu {
                display: none;
            }

            .mobile-menu-btn {
                display: flex;
            }

            .hero {
                min-height: 70vh;
                padding: 2rem 1rem;
            }

            .hero h1 {
                font-size: 1.8rem;
            }

            .hero p {
                font-size: 1rem;
            }

            section {
                padding: 2rem 1rem;
            }

            section h2 {
                font-size: 1.6rem;
                margin-bottom: 2rem;
            }

            .programs-grid {
                grid-template-columns: 1fr;
                gap: 1.5rem;
            }

            .action-links {
                flex-direction: column;
                gap: 0.8rem;
            }

            .action-links a {
                padding: 0.8rem 1.5rem;
                width: 100%;
                text-align: center;
            }

            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 1rem;
            }

            .stat-card {
                padding: 1.5rem 0.8rem;
            }

            .stat-number {
                font-size: 2rem;
            }

            .stat-label {
                font-size: 0.95rem;
            }

            .testimonials-grid {
                grid-template-columns: 1fr;
                gap: 1.5rem;
            }

            .container {
                padding: 0 1rem;
            }

            footer .links {
                flex-direction: column;
                gap: 1rem;
            }
        }

        @media (max-width: 480px) {
            nav {
                padding: 0.6rem 0.8rem;
            }

            nav .logo img {
                height: 40px;
            }

            .hero {
                min-height: 60vh;
                padding: 1.5rem 1rem;
            }

            .hero h1 {
                font-size: 1.4rem;
                margin-bottom: 1rem;
            }

            .hero p {
                font-size: 0.95rem;
                margin-bottom: 1.5rem;
            }

            .cta-button {
                padding: 0.7rem 1.8rem;
                font-size: 0.9rem;
            }

            section {
                padding: 1.5rem 1rem;
            }

            section h2 {
                font-size: 1.3rem;
                margin-bottom: 1.5rem;
            }

            .what-we-do p {
                font-size: 0.95rem;
            }

            .program-card {
                padding: 1.5rem;
            }

            .program-card h3 {
                font-size: 1.1rem;
            }

            .program-card p {
                font-size: 0.9rem;
            }

            .statistics {
                padding: 3rem 1rem;
            }

            .statistics h2 {
                font-size: 1.5rem;
            }

            .stats-grid {
                grid-template-columns: 1fr;
                gap: 0.8rem;
            }

            .stat-number {
                font-size: 1.8rem;
            }

            .stat-label {
                font-size: 0.85rem;
            }

            .testimonial-card {
                padding: 1.5rem;
            }

            .testimonial-quote {
                font-size: 0.95rem;
            }

            .cta-section {
                padding: 2rem 1rem;
            }

            .cta-section h2 {
                font-size: 1.3rem;
            }

            footer {
                padding: 2rem 1rem;
            }

            footer p {
                font-size: 0.85rem;
            }
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav>
        <div class="container">
            <a href="/" class="logo">
                <img src="/static/logo.svg" alt="NexYouth">
            </a>
            <button class="mobile-menu-btn" id="mobileMenuBtn">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul id="navMenu">
                <li><a href="/">Home</a></li>
                <li><a href="/#what-we-do">What We Do</a></li>
                <li class="dropdown">
                    <a href="/#programs">Programs ▾</a>
                    <div class="dropdown-menu" id="programsDropdown">
                        <a href="/programs/skill-development">Skill Development Courses</a>
                        <a href="/programs/seminars">Expert Seminars & Talks</a>
                        <a href="/programs/mentorship">Global Mentorship Network</a>
                        <a href="/programs/environmental-competition">Environmental Youth Competition</a>
                    </div>
                </li>
                <li><a href="/#community">Community</a></li>
                <li><a href="/partner">Partner</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <video autoplay muted loop playsinline>
            <source src="/static/main_background.mp4" type="video/mp4">
        </video>
        <div class="content">
            <h1> Creating Space for Youth. Shaping Futures.</h1>
            <p>Connect with mentors, develop in-demand skills, and unlock global opportunities</p>
            <a href="#what-we-do" class="cta-button">Learn More</a>
        </div>
    </section>

    <!-- What We Do Section -->
    <section id="what-we-do" class="what-we-do">
        <div class="container">
            <h2>What We Do</h2>
            <p>At NexYouth, we're on a mission to empower young people globally through skill development, mentorship, and community. We connect youth with industry experts, provide practical training, and create pathways to success in an ever-changing world.</p>
            <div class="action-links">
                <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform?pli=1" target="_blank">Get Involved</a>
            </div>
        </div>
    </section>

    <!-- Programs Section -->
    <section id="programs" class="programs">
        <div class="container">
            <h2>Featured Programs</h2>
            <div class="programs-grid">
                <a href="/programs/skill-development" class="program-card" style="text-decoration: none; color: inherit;">
                    <h3>Skill Development Courses</h3>
                    <p>Comprehensive training programs that equip youth with practical skills and real-world opportunities. From digital literacy, environmental analysis to entrepreneurship, our courses prepare students for real-world success.</p>
                </a>
                <a href="/programs/seminars" class="program-card" style="text-decoration: none; color: inherit;">
                    <h3>Expert Seminars & Talks</h3>
                    <p>Learn directly from industry leaders and experienced professionals. Our seminars provide insights into emerging opportunities and inspire the next generation of innovators.</p>
                </a>
                <a href="/programs/mentorship" class="program-card" style="text-decoration: none; color: inherit;">
                    <h3>Global Mentorship Network</h3>
                    <p>Get paired with mentors who can guide your personal and professional development. Our mentors bring real-world experience and genuine commitment to your growth.</p>
                </a>
                <a href="/programs/environmental-competition" class="program-card" style="text-decoration: none; color: inherit;">
                    <h3>Environmental Youth Competition</h3>
                    <p>Compete globally with young innovators to investigate real-world environmental challenges through research and data analysis. Tackle local environmental issues with actionable insights through essays, analytical reports, research, and win scholarships!</p>
                </a>
            </div>
        </div>
    </section>

    <!-- Statistics Section -->
    <section class="statistics">
        <div class="container">
            <h2>Our Impact</h2>
            <p>Making a difference across the globe through youth empowerment</p>
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number">5000+</div>
                    <div class="stat-label">Individuals Reached</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">90+</div>
                    <div class="stat-label">Schools Represented</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">13+</div>
                    <div class="stat-label">Countries Reached</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">26+</div>
                    <div class="stat-label">Cities of Operation</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">700+</div>
                    <div class="stat-label">Students Taught</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">12+</div>
                    <div class="stat-label">States & Provinces</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Community Section -->
    <section id="community" class="testimonials">
        <div class="container">
            <h2>Words From Our Community</h2>
            <div class="testimonials-grid">
                <div class="testimonial-card">
                    <div class="testimonial-quote">"NexYouth completely transformed my perspective on personal development. The mentorship I received helped me navigate challenges and achieve my goals."</div>
                    <div class="testimonial-author">Sarah J.</div>
                    <div class="testimonial-title">Course Participant</div>
                </div>
                <div class="testimonial-card">
                    <div class="testimonial-quote">"Being part of this community showed me that I'm not alone in my journey. The support and guidance from mentors made all the difference in my success."</div>
                    <div class="testimonial-author">Marcus C.</div>
                    <div class="testimonial-title">Program Graduate</div>
                </div>
                <div class="testimonial-card">
                    <div class="testimonial-quote">"The practical skills and confidence I gained through NexYouth's programs have been instrumental in landing my dream internship and building my career."</div>
                    <div class="testimonial-author">Amina P.</div>
                    <div class="testimonial-title">Scholarship Winner</div>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section id="contact" class="cta-section">
        <div class="container">
            <h2>Join Our Community Today</h2>
            <p style="font-size: 1.1rem; margin-bottom: 2rem;">Ready to start your journey? Join us now!</p>
            <div class="action-links" style="justify-content: center;">
                <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform?pli=1" target="_blank" style="color: #ff6b35;">Get Involved</a>
    <footer id="contact-footer">
        <div class="container">
            <p>&copy; 2023 NexYouth. All rights reserved.</p>
        </div>
    </footer>

    <script>
        // Mobile menu functionality
        const mobileMenuBtn = document.getElementById('mobileMenuBtn');
        const navMenu = document.getElementById('navMenu');
        const programsDropdown = document.querySelector('.dropdown a');
        const dropdownMenu = document.getElementById('programsDropdown');

        mobileMenuBtn.addEventListener('click', () => {
            mobileMenuBtn.classList.toggle('active');
            navMenu.classList.toggle('active');
        });

        // Close menu when clicking on a link
        const navLinks = document.querySelectorAll('#navMenu a:not([href*="Programs"])');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileMenuBtn.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });

        // Handle programs dropdown on mobile
        const dropdownTrigger = document.querySelector('.dropdown a');
        dropdownTrigger.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                dropdownMenu.classList.toggle('active');
            }
        });

        // Handle dropdown menu items click on mobile
        const dropdownItems = document.querySelectorAll('.dropdown-menu a');
        dropdownItems.forEach(item => {
            item.addEventListener('click', (e) => {
                if (window.innerWidth <= 768) {
                    // Close menu but allow navigation to proceed
                    mobileMenuBtn.classList.remove('active');
                    navMenu.classList.remove('active');
                    dropdownMenu.classList.remove('active');
                    // Let the link navigate
                }
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!e.target.closest('nav')) {
                mobileMenuBtn.classList.remove('active');
                navMenu.classList.remove('active');
                dropdownMenu.classList.remove('active');
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template('index.html')

# ============== ABOUT PAGE ==============
ABOUT_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="NexYouth - Meet our team of passionate youth leaders.">
    <title>About Us - NexYouth</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #fff;
        }

        /* Navigation */
        nav {
            background: white;
            border-bottom: 1px solid #eee;
            position: sticky;
            top: 0;
            z-index: 50;
            padding: 0.8rem 2rem;
        }

        nav .container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        nav .logo {
            display: flex;
            align-items: center;
            text-decoration: none;
        }

        nav .logo img {
            height: 70px;
            width: auto;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        nav li {
            position: relative;
        }

        nav a {
            text-decoration: none;
            color: #333;
            font-size: 1rem;
            font-weight: 500;
            transition: color 0.2s;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        nav a:hover {
            color: #00d4ff;
        }

        /* Dropdown Menu */
        .dropdown-menu {
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            min-width: 220px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            padding: 0.5rem 0;
            z-index: 100;
        }

        .dropdown:hover .dropdown-menu {
            display: block;
        }

        .dropdown-menu a {
            display: block;
            padding: 0.8rem 1.2rem;
            font-size: 0.9rem;
            text-transform: none;
            letter-spacing: 0;
        }

        .dropdown-menu a:hover {
            background: #f5f5f5;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #0d2137 100%);
            color: white;
            text-align: center;
            padding: 6rem 2rem;
        }

        .hero h1 {
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 1rem;
        }

        .hero p {
            font-size: 1.2rem;
            max-width: 700px;
            margin: 0 auto;
            opacity: 0.9;
        }

        /* Who We Are Section */
        .who-we-are {
            padding: 6rem 2rem;
            background: white;
        }

        .who-we-are h2 {
            font-size: 2.5rem;
            margin-bottom: 2rem;
            color: #1a1a2e;
            text-align: center;
        }

        .who-we-are-content {
            display: grid;
            grid-template-columns: 1.2fr 1fr;
            gap: 4rem;
            align-items: center;
            margin-bottom: 3rem;
        }

        .who-we-are-text {
            text-align: center;
        }

        .who-we-are-text {
            text-align: left;
        }

        .who-we-are-text p {
            font-size: 1.05rem;
            line-height: 1.8;
            color: #555;
            margin-bottom: 1.5rem;
        }

        .who-we-are-featured {
            text-align: center;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
        }

        .featured-founder {
            text-align: center;
        }

        .featured-founder img {
            width: 180px;
            height: 180px;
            object-fit: cover;
            border-radius: 50%;
            margin: 0 auto 1.5rem;
            display: block;
            box-shadow: 0 5px 20px rgba(0, 212, 255, 0.2);
        }

        .featured-founder h3 {
            font-size: 1.3rem;
            color: #1a1a2e;
            margin-bottom: 0.5rem;
        }

        .featured-founder .title {
            color: #00d4ff;
            font-weight: 600;
            font-size: 0.9rem;
            margin-bottom: 1rem;
            display: block;
        }

        .featured-founder p {
            font-size: 0.9rem;
            color: #666;
            line-height: 1.6;
        }

        .who-we-are-featured img {
            width: 180px;
            height: 180px;
            object-fit: cover;
            border-radius: 50%;
            margin: 0 auto 1.5rem;
            display: block;
            box-shadow: 0 5px 20px rgba(0, 212, 255, 0.2);
        }

        .who-we-are-featured h3 {
            font-size: 1.4rem;
            color: #1a1a2e;
            margin-bottom: 0.5rem;
        }

        .who-we-are-featured .title {
            color: #00d4ff;
            font-weight: 600;
            font-size: 0.95rem;
            margin-bottom: 1rem;
        }

        .who-we-are-featured p {
            font-size: 0.95rem;
            color: #666;
            line-height: 1.6;
        }

        /* Our Story Section */
        .our-story {
            padding: 6rem 2rem;
            background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);
        }

        .our-story h2 {
            font-size: 2.5rem;
            margin-bottom: 2rem;
            color: #1a1a2e;
            text-align: center;
        }

        .our-story-content {
            display: grid;
            grid-template-columns: 1fr;
            gap: 4rem;
            align-items: center;
        }

        .our-story-text {
            text-align: left;
            max-width: 900px;
            margin: 0 auto;
        }

        .our-story-text p {
            font-size: 1.05rem;
            line-height: 1.8;
            color: #555;
            margin-bottom: 1.5rem;
        }

        .our-story-text p:last-child {
            margin-bottom: 0;
        }

        .our-story-image img {
            width: 100%;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }

        /* What We Do Section */
        .what-we-do {
            padding: 6rem 2rem;
            background: white;
        }

        .what-we-do h2 {
            font-size: 2.5rem;
            margin-bottom: 2rem;
            color: #1a1a2e;
            text-align: center;
        }

        .what-we-do-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            align-items: start;
        }

        .what-we-do-text {
            text-align: left;
            max-width: 900px;
            margin: 0 auto;
        }

        .what-we-do-text p {
            font-size: 1.05rem;
            line-height: 1.8;
            color: #555;
            margin-bottom: 1.5rem;
        }

        .what-we-do-text p:last-child {
            margin-bottom: 0;
        }

        .what-we-do-image img {
            width: 100%;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }

        /* Leadership Section */
        .leadership {
            padding: 6rem 2rem;
            background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);
        }

        .leadership h2 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            text-align: center;
            color: #1a1a2e;
        }

        .leadership > .container > p {
            text-align: center;
            color: #666;
            font-size: 1.05rem;
            max-width: 700px;
            margin: 0 auto 3rem;
            line-height: 1.7;
        }

        .team-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2.5rem;
        }

        .team-member {
            text-align: center;
            background: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            transition: all 0.3s ease;
        }

        .team-member:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.12);
        }

        .team-member-image {
            width: 180px;
            height: 180px;
            border-radius: 50%;
            margin: 0 auto 1.5rem;
            background: linear-gradient(135deg, #e8f9ff 0%, #d0f0ff 100%);
            overflow: hidden;
            box-shadow: 0 5px 20px rgba(0, 212, 255, 0.2);
        }

        .team-member-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .team-member h3 {
            font-size: 1.2rem;
            color: #1a1a2e;
            margin-bottom: 0.5rem;
            font-weight: 700;
        }

        .team-member .title {
            color: #00d4ff;
            font-weight: 600;
            font-size: 0.9rem;
            margin-bottom: 1rem;
            display: block;
        }

        .team-member .bio {
            font-size: 0.95rem;
            line-height: 1.6;
            color: #666;
            margin-bottom: 1.5rem;
        }

        .team-member .social-link {
            display: inline-block;
            color: #00d4ff;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.85rem;
        }

        .team-member .social-link:hover {
            text-decoration: underline;
        }

        /* CTA Section */
        .cta-section {
            background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #0d2137 100%);
            color: white;
            text-align: center;
            padding: 6rem 2rem;
        }

        .cta-section h2 {
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
            color: white;
        }

        .cta-section p {
            font-size: 1.1rem;
            margin-bottom: 2rem;
            opacity: 0.9;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }

        .cta-btn {
            display: inline-block;
            background: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%);
            color: white;
            padding: 1rem 2.5rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s ease;
            box-shadow: 0 5px 20px rgba(0, 212, 255, 0.3);
        }

        .cta-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(0, 212, 255, 0.4);
        }

        footer {
            background: #000;
            color: white;
            padding: 3rem 2rem;
            text-align: center;
        }

        footer p {
            color: #999;
            font-size: 0.9rem;
        }

        @media (max-width: 768px) {
            nav {
                padding: 0.8rem 1rem;
            }

            nav .logo img {
                height: 50px;
            }

            nav ul {
                display: none;
                flex-direction: column;
                position: absolute;
                top: 100%;
                left: 0;
                right: 0;
                background: white;
                gap: 0;
                border-top: 1px solid #eee;
            }

            nav ul.active {
                display: flex;
            }

            nav li {
                width: 100%;
                position: relative;
            }

            nav a {
                display: block;
                padding: 1rem 2rem;
                font-size: 0.9rem;
                text-transform: uppercase;
            }

            .dropdown-menu {
                position: static;
                display: none;
                box-shadow: none;
                background: #f5f5f5;
                border-radius: 0;
                min-width: auto;
            }

            .dropdown-menu.active {
                display: block;
            }

            .dropdown-menu a {
                padding: 0.6rem 2rem 0.6rem 3rem;
                font-size: 0.85rem;
            }

            .dropdown:hover .dropdown-menu {
                display: none;
            }

            .mobile-menu-btn {
                display: flex;
            }

            .hero h1 {
                font-size: 2rem;
            }

            .who-we-are-content,
            .our-story-content,
            .what-we-do-content {
                grid-template-columns: 1fr;
                gap: 2rem;
            }

            .team-grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .cta-section h2 {
                font-size: 1.8rem;
            }
        }
    </style>
</head>
<body>
    <nav>
        <div class="container">
            <a href="/" class="logo">
                <img src="/static/logo.svg" alt="NexYouth">
            </a>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/#what-we-do">What We Do</a></li>
                <li class="dropdown">
                    <a href="/#programs">Programs ▾</a>
                    <div class="dropdown-menu">
                        <a href="/programs/skill-development">Skill Development Courses</a>
                        <a href="/programs/seminars">Expert Seminars & Talks</a>
                        <a href="/programs/mentorship">Global Mentorship Network</a>
                        <a href="/programs/environmental-competition">Environmental Youth Competition</a>
                    </div>
                </li>
                <li><a href="/#community">Community</a></li>
                <li><a href="/partner">Partner</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h1>The Team Behind NexYouth</h1>
            <p>At the heart of NexYouth is our inspiring community of volunteers — passionate individuals who dedicate their time, skills, and creativity to driving meaningful change. Coming from diverse backgrounds in science, education, advocacy, and the arts, our volunteers share a common commitment to protecting the environment and empowering youth.</p>
        </div>
    </section>

    <!-- Who We Are Section -->
    <section class="who-we-are">
        <div class="container">
            <h2>Who We Are</h2>
            
            <div class="who-we-are-content">
                <div class="who-we-are-text">
                    <p>NexYouth was founded by a small group of high school students who recognized gaps in educational access and sought to address them through peer-led action. What began as a student initiative has grown into a youth-run nonprofit supporting students across diverse backgrounds through education, mentorship, and service.</p>
                    <p>Our work is grounded in the belief that young people are not only beneficiaries of change, but capable leaders in creating it. Through partnerships with schools, community organizations, and youth groups, NexYouth provides structured opportunities for students to develop academic skills, leadership capacity, and a sense of civic responsibility.</p>
                    <p>Led entirely by students, our organization emphasizes sustainable impact, collaboration, and access. By lowering barriers to quality learning and leadership opportunities, NexYouth aims to equip young people with the confidence, skills, and perspective needed to contribute meaningfully to their communities and beyond.</p>
                </div>

                <div class="who-we-are-featured">
                    <div class="featured-founder">
                        <img src="https://www.nexyouth.org/Member_Jhuan1.jpg" alt="Justin Huang - Co-Founder" onerror="this.src='/static/placeholder.jpg'">
                        <h3>Justin Huang</h3>
                        <span class="title">Co-Founder</span>
                        <p>Justin is passionate about experiential learning and believes every youth deserves access to meaningful opportunities. As co-founder and president, he oversees strategic partnerships and expansion initiatives.</p>
                    </div>

                    <div class="featured-founder">
                        <img src="https://www.nexyouth.org/Member_Mwen1.jpg" alt="Max Wen - Co-Founder" onerror="this.src='/static/placeholder.jpg'">
                        <h3>Max Wen</h3>
                        <span class="title">Co-Founder</span>
                        <p>Max co-founded NexYouth with a vision to democratize access to quality education and mentorship for youth globally. Passionate about creating systemic change through youth empowerment.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Our Story Section -->
    <section class="our-story">
        <div class="container">
            <h2>Our Story</h2>
            <div class="our-story-content">
                <div class="our-story-text">
                    <p>NexYouth was founded in 2023 by high school students whose experiences during the COVID-19 pandemic reshaped how they viewed education, access, and youth leadership. As schools moved online and support systems became uneven, our founders saw firsthand how many young people were left without guidance, structure, or opportunities to grow.</p>
                    <p>Motivated by this experience, NexYouth began as a youth-led initiative focused on creating spaces where students could reconnect, develop skills, and take initiative. What started with a small group of volunteers has since grown into a broader youth network spanning multiple countries.</p>
                    <p>Today, NexYouth is built on a simple belief: young people are capable of leading meaningful change when given responsibility, trust, and the chance. Through youth-designed programs and partnerships with schools and community organizations, we work to expand access to learning opportunities and leadership experiences, while empowering students to support one another and contribute with purpose.</p>
                </div>
                <div class="our-story-image">
                    <img src="/static/main_background.mp4" alt="NexYouth Community" onerror="this.style.display='none'">
                </div>
            </div>
        </div>
    </section>

    <!-- What We Do Section -->
    <section class="what-we-do">
        <div class="container">
            <h2>What We Do</h2>
            <div class="what-we-do-content">
                <div class="what-we-do-text">
                    <p>We operate three core programs designed to serve young people at different stages of their journey:</p>
                    <p><strong>Skill Development Courses:</strong> Our comprehensive courses cover essential topics from public speaking to STEM, delivered by passionate instructors committed to youth success.</p>
                    <p><strong>Expert Seminars & Talks:</strong> We bring industry leaders and experts together with young people for interactive sessions on emerging opportunities and global challenges.</p>
                    <p><strong>Global Mentorship Network:</strong> Our mentorship program connects youth with experienced professionals worldwide who provide personalized guidance and support for career development and personal growth.</p>
                    <p>Beyond these programs, we're constantly innovating and listening to the youth we serve to develop initiatives that have real, lasting impact.</p>
                </div>
                <div class="what-we-do-image">
                    <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?w=500&h=400&fit=crop" alt="NexYouth Programs" onerror="this.style.display='none'">
                </div>
            </div>
        </div>
    </section>

    <!-- Leadership Section -->
    <section class="leadership">
        <div class="container">
            <h2>Our Leadership</h2>
            <p>Our leadership team is comprised of passionate youth leaders from across the globe, each bringing unique expertise and a commitment to youth empowerment. They guide NexYouth's vision and strategy.</p>

            <div class="team-grid">
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Jhuan1.jpg" alt="Justin Huang" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>Justin Huang</h3>
                    <span class="title">Co-Founder</span>
                    <p>Justin is the co-founder of NexYouth. He is interested in how young people learn through experience, connection, and initiative, and focuses on creating spaces where youth can explore ideas and take ownership of what they care about.</p>
                </div>

                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Mwen1.jpg" alt="Max Wen" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>Max Wen</h3>
                    <span class="title">Co-Founder</span>
                    <p>Max is dedicated to making youth development accessible globally. With expertise in program design, he drives innovation in our initiatives and curriculum.</p>
                </div>

                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Suzea1.png" alt="Stephanie Uzea" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>Stephanie Uzea</h3>
                    <span class="title">Canada President & Director of Operations</span>
                    <p>Stephanie brings strategic vision and operational excellence to NexYouth. As Canada President and Director of Operations, she oversees Canadian operations and manages our growing team of volunteers and partners.</p>
                </div>

                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Xyang1.jpg" alt="Xuhan Yang" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>Xuhan Yang</h3>
                    <span class="title">Director of Technology</span>
                    <p>Xuhan, as Director of Technology, oversees our technology initiatives, developing digital solutions to make NexYouth's programs accessible to youth around the world. Passionate about innovation and impact.</p>
                </div>

                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Eluo1.png" alt="Ethan Luo" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>Ethan Luo</h3>
                    <span class="title">Oakville Chapter President</span>
                    <p>Ethan is a Grade 10 student at Abbey Park High School in Oakville. With 2 years of competitive debate experience, he has advanced at prestigious tournaments such as Harvard WSDC, Queens BPHS, McGill BPHS, and Hart House High Schools. Outside debate, he enjoys clarinet, trail running, and co-hosting Perception Podcast.</p>
                </div>

                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Rwei1.png" alt="Rachel Wei" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>Rachel Wei</h3>
                    <span class="title">Coquitlam Chapter President</span>
                    <p>Rachel, as president of the Coquitlam Chapter, oversees the chapter and is instrumental in building community connections. She's dedicated to making NexYouth's programs accessible to local youth.</p>
                </div>

                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Chuan1.jpg" alt="Chloe Huang" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>Chloe Huang</h3>
                    <span class="title">Secretary</span>
                    <p>Chloe is a Grade 11 student at Earl of March High School. She is an avid volleyball player and loves sports!</p>
                </div>

                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Kjosh1.png" alt="Keerti Joshi" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>Keerti Joshi</h3>
                    <span class="title">Debate Coach</span>
                    <p>I'm Keerti, I'm a grade 11 student at Upper Canada College. I've been debating since Grade 8 and I debate in both WSDC and BP formats. I am a new member of the Canadian National Debating Team.</p>
                </div>

                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Kyip1.png" alt="Kristen Yip" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>Kristen Yip</h3>
                    <span class="title">Debate Coach</span>
                    <p>Kristen Y (she/her) is a grade 9 student and avid debater. Achievements include: Top 4th speaker+top jr speaker (Harthouse Winter Open), top 3rd speaker + grand finalist (Harthouse Summer Open).</p>
                </div>

                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Czhan1.png" alt="Cody Zhang" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>Cody Zhang</h3>
                    <span class="title">Economics Instructor</span>
                    <p>Cody Zhang is a high schooler from Toronto and scored a 5 on AP Micro and makes economics simple, fun, and engaging!</p>
                </div>

                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Jliu1.png" alt="Jeffrey Liu" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>Jeffrey Liu</h3>
                    <span class="title">Debate Coach</span>
                    <p>Hi, I'm Jeffrey! I am a grade 11 student at Milliken Mills High School. In my free time I love cooking food, listening to music, and working out! Passionate about accessibility in debate.</p>
                </div>

                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Aliu1.png" alt="Amy Liu" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>Amy Liu</h3>
                    <span class="title">Debate Coach</span>
                    <p>Amy is a G10 student and a competitive debater who has won many debate tournaments.</p>
                </div>

                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Fzhan1.jpg" alt="Ferrari Zhang" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>Ferrari Zhang</h3>
                    <span class="title">Debate Coach</span>
                    <p>Ferrari is a G10 student and a competitive debater, who loves argumentation and refutation!</p>
                </div>

                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Tguo1.png" alt="Terrence Guo" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>Terrence Guo</h3>
                    <span class="title">Debate Coach</span>
                    <p>Terrence is a G12 student and a competitive debater at the national level, winning many debating tournaments, including being the top speaker at Hart House High Schools.</p>
                </div>

                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Yshua1.png" alt="Yunfei Shuai" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>Yunfei Shuai</h3>
                    <span class="title">Contests Organizer</span>
                    <p>Yunfei wrote her first story when she was 7 years old and never looked back since. She is an avid sci-fi enthusiast and an aspiring astrophysicist.</p>
                </div>

                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Szhen1.png" alt="Susan Zheng" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>Susan Zheng</h3>
                    <span class="title">Contests Organizer</span>
                    <p>Susan finds way too much enjoyment in daydreaming about fictional scenarios and promising herself she'll finish a project tomorrow. A sci-fi fanatic, she obsesses over specific concepts.</p>
                </div>

                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Sisla1.png" alt="Shahrad Islam" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>Shahrad Islam</h3>
                    <span class="title">Science Instructor</span>
                    <p>Hi! My name is Shahrad! Some things you should know about me are that I like playing sports, playing instruments, watching movies and shows, and I really like cats!</p>
                </div>

                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Rliu1.png" alt="Ronnie Liu" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>Ronnie Liu</h3>
                    <span class="title">Science Instructor</span>
                    <p>Hello, my name is Ronnie Liu. I am a gifted grade 10 scholar at Richmond Hill High School. I love teaching because I enjoy watching children learn and discover new things.</p>
                </div>

                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://nexyouth-eight.vercel.app/static/AaronYang.jpg" alt="Aaron Yang" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>Aaron Yang</h3>
                    <span class="title">Debate Coach</span>
                    <p>Aaron is a high school student at University of Toronto Schools with a strong passion about Debate and Competitive Programming. Has been competing for 3 years and is the only junior-qualifying senior national semifinalist in recent years. Achievements include top performer in age group at Harvard World Schools and Hart House Junior Quarterfinalist. Outside of debate, enjoys ultimate frisbee and exploring Classics.</p>
                </div>

                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://nexyouth-eight.vercel.app/static/VincentPham.jpg" alt="Vincent Pham" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>Vincent Pham</h3>
                    <span class="title">Coding Instructor</span>
                    <p>Vincent is an IB Grade 11 student from Ottawa who enjoys building projects ranging from websites and games to apps and machine learning. He is proficient in full-stack development, Python, and Swift, and has performed well in several Canadian computer science competitions. Outside of coding, he is an award-winning violinist and enjoys running with his goldendoodle, Isabelle.</p>
                </div>

                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://nexyouth-eight.vercel.app/static/WilliamWang.jpg" alt="William Wang" onerror="this.src='/static/placeholder.jpg'">
                    </div>
                    <h3>William Wang</h3>
                    <span class="title">Coding Instructor</span>
                    <p>William Wang is a high school student at University of Toronto Schools with a strong interest in STEM. He enjoys exploring coding and problem-solving and is excited to help students build a solid foundation in programming through NexYouth.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
        <div class="container">
            <h2>Join Our Movement</h2>
            <p>Whether you're a young person looking to develop skills, a professional wanting to mentor, or an organization interested in partnering with us, we'd love to hear from you.</p>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform?pli=1" class="cta-btn">Get Involved</a>
        <div class="container">
            <p>&copy; 2023 NexYouth. All rights reserved. | Grow • Lead • Act</p>
        </div>
    </footer>
</body>
</html>
"""

@app.route('/about')
def about():
    return render_template('about.html')

# Program Page Templates
SKILL_DEVELOPMENT_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skill Development Courses - NexYouth</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #fff;
        }

        nav {
            background: white;
            border-bottom: 1px solid #eee;
            position: sticky;
            top: 0;
            z-index: 50;
            padding: 0.8rem 2rem;
        }

        nav .container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        nav .logo {
            display: flex;
            align-items: center;
            text-decoration: none;
        }

        nav .logo img {
            height: 70px;
            width: auto;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        nav ul li {
            position: relative;
        }

        nav a {
            text-decoration: none;
            color: #333;
            font-size: 1rem;
            font-weight: 500;
            transition: color 0.2s;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        nav a:hover {
            color: #00d4ff;
        }

        /* Dropdown Menu */
        .dropdown-menu {
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            min-width: 220px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            padding: 0.5rem 0;
            z-index: 100;
        }

        .dropdown:hover .dropdown-menu {
            display: block;
        }

        .dropdown-menu a {
            display: block;
            padding: 0.8rem 1.2rem;
            font-size: 0.9rem;
            text-transform: none;
            letter-spacing: 0;
            color: #333;
        }

        .dropdown-menu a:hover {
            background: #f5f5f5;
            color: #00d4ff;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .program-hero {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: white;
            text-align: center;
            padding: 6rem 2rem;
        }

        .program-hero h1 {
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
        }

        .program-hero p {
            font-size: 1.2rem;
            max-width: 800px;
            margin: 0 auto;
            opacity: 0.9;
            line-height: 1.8;
        }

        .program-content {
            padding: 5rem 2rem;
        }

        .program-content h2 {
            font-size: 2rem;
            margin-bottom: 1.5rem;
            color: #1a1a2e;
        }

        .program-content p {
            font-size: 1.1rem;
            line-height: 1.8;
            margin-bottom: 1.5rem;
            color: #555;
        }

        .courses-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .course-card {
            background: white;
            border-radius: 12px;
            padding: 2rem;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            transition: transform 0.3s, box-shadow 0.3s;
            border-left: 4px solid #00d4ff;
        }

        .course-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
        }

        .course-card h3 {
            font-size: 1.3rem;
            margin-bottom: 1rem;
            color: #1a1a2e;
        }

        .course-card p {
            font-size: 1rem;
            color: #666;
            margin-bottom: 0;
        }

        .cta-section {
            background: #00d4ff;
            color: white;
            text-align: center;
            padding: 4rem 2rem;
        }

        .cta-section h2 {
            font-size: 2rem;
            margin-bottom: 1rem;
            color: white;
        }

        .cta-section p {
            font-size: 1.1rem;
            margin-bottom: 2rem;
            opacity: 0.95;
        }

        .cta-btn {
            display: inline-block;
            background: white;
            color: #00d4ff;
            padding: 1rem 2.5rem;
            border-radius: 4px;
            text-decoration: none;
            font-weight: 600;
            transition: transform 0.2s;
        }

        .cta-btn:hover {
            transform: translateY(-2px);
        }

        footer {
            background: #000;
            color: white;
            padding: 3rem 2rem;
            text-align: center;
        }

        footer .links {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }

        footer a {
            color: #fff;
            text-decoration: none;
            font-size: 0.95rem;
        }

        footer a:hover {
            color: #00d4ff;
        }

        footer p {
            color: #999;
            font-size: 0.9rem;
        }

        @media (max-width: 768px) {
            .program-hero h1 {
                font-size: 2rem;
            }
            nav ul {
                gap: 1rem;
                flex-wrap: wrap;
                justify-content: center;
            }
            nav .container {
                flex-direction: column;
                gap: 1rem;
            }
        }
    </style>
</head>
<body>
    <nav>
        <div class="container">
            <a href="/" class="logo">
                <img src="/static/logo.svg" alt="NexYouth">
            </a>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/#what-we-do">What We Do</a></li>
                <li class="dropdown">
                    <a href="/#programs">Programs ▾</a>
                    <div class="dropdown-menu">
                        <a href="/programs/skill-development">Skill Development Courses</a>
                        <a href="/programs/seminars">Expert Seminars & Talks</a>
                        <a href="/programs/mentorship">Global Mentorship Network</a>
                        <a href="/programs/environmental-competition">Environmental Youth Competition</a>
                    </div>
                </li>
                <li><a href="/#community">Community</a></li>
                <li><a href="/partner">Partner</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <section class="program-hero">
        <div class="container">
            <h1>Skill Development Courses</h1>
            <p>Empowering youth with the skills and perspective to lead in the future.Programs grounded in critical thinking, environmental understanding, data literacy, and STEM.</p>
        </div>
    </section>

    <section class="program-content">
        <div class="container">
            <h2>Our Course Offerings</h2>
            <p>We offer a wide range of courses designed to equip young people with the skills they need to make a difference in their communities and beyond. Each course is led by experienced instructors passionate about youth development.</p>

            <div class="courses-grid">
                <div class="course-card">
                    <h3>Public Speaking & Debate</h3>
                    <p>Build confidence and communication skills through structured debate training and public speaking exercises. Perfect for future leaders and advocates.</p>
                </div>
                <div class="course-card">
                    <h3>Environmental Science</h3>
                    <p>Explore the science behind climate change, ecosystems, and sustainability. Learn how to analyze environmental data and propose solutions.</p>
                </div>
                <div class="course-card">
                    <h3>Leadership & Team Building</h3>
                    <p>Develop essential leadership skills through hands-on activities and real-world projects. Learn to inspire and motivate teams effectively.</p>
                </div>
                <div class="course-card">
                    <h3>STEM Fundamentals</h3>
                    <p>Guided sessions to science, technology, engineering, and mathematics through discussion, mentorship, and projects.</p>
                </div>
                <div class="course-card">
                    <h3>Content Creation</h3>
                    <p>Learn video editing, social media strategy, and digital storytelling to amplify your message and reach broader audiences.</p>
                </div>
                <div class="course-card">
                    <h3>Project Management</h3>
                    <p>Master the fundamentals of planning, executing, and delivering impactful community projects from start to finish.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="cta-section">
        <div class="container">
            <h2>Ready to Start Learning?</h2>
            <p>Join our next cohort and develop skills that will last a lifetime.</p>
            <a href="https://forms.gle/YxCWJ32dZJTofHREA" target="_blank" class="cta-btn">Enroll Now</a>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2023 NexYouth. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

SEMINARS_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expert Seminars & Talks - NexYouth</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #fff;
        }

        nav {
            background: white;
            border-bottom: 1px solid #eee;
            position: sticky;
            top: 0;
            z-index: 50;
            padding: 0.8rem 2rem;
        }

        nav .container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        nav .logo {
            display: flex;
            align-items: center;
            text-decoration: none;
        }

        nav .logo img {
            height: 70px;
            width: auto;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        nav ul li {
            position: relative;
        }

        nav a {
            text-decoration: none;
            color: #333;
            font-size: 1rem;
            font-weight: 500;
            transition: color 0.2s;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        nav a:hover {
            color: #00d4ff;
        }

        /* Dropdown Menu */
        .dropdown-menu {
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            min-width: 220px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            padding: 0.5rem 0;
            z-index: 100;
        }

        .dropdown:hover .dropdown-menu {
            display: block;
        }

        .dropdown-menu a {
            display: block;
            padding: 0.8rem 1.2rem;
            font-size: 0.9rem;
            text-transform: none;
            letter-spacing: 0;
            color: #333;
        }

        .dropdown-menu a:hover {
            background: #f5f5f5;
            color: #00d4ff;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .program-hero {
            background: linear-gradient(135deg, #0d9488 0%, #14b8a6 100%);
            color: white;
            text-align: center;
            padding: 6rem 2rem;
        }

        .program-hero h1 {
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
        }

        .program-hero p {
            font-size: 1.2rem;
            max-width: 800px;
            margin: 0 auto;
            opacity: 0.95;
            line-height: 1.8;
        }

        .program-content {
            padding: 5rem 2rem;
        }

        .program-content h2 {
            font-size: 2rem;
            margin-bottom: 1.5rem;
            color: #1a1a2e;
        }

        .program-content p {
            font-size: 1.1rem;
            line-height: 1.8;
            margin-bottom: 1.5rem;
            color: #555;
        }

        .seminars-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .seminar-card {
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .seminar-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
        }

        .seminar-card-header {
            background: linear-gradient(135deg, #0d9488 0%, #14b8a6 100%);
            color: white;
            padding: 1.5rem;
        }

        .seminar-card-header h3 {
            font-size: 1.3rem;
            margin-bottom: 0.5rem;
        }

        .seminar-card-header span {
            font-size: 0.9rem;
            opacity: 0.9;
        }

        .seminar-card-body {
            padding: 1.5rem;
        }

        .seminar-card-body p {
            font-size: 1rem;
            color: #666;
            margin-bottom: 0;
        }

        .topics-section {
            background: #f9f9f9;
            padding: 5rem 2rem;
        }

        .topics-section h2 {
            font-size: 2rem;
            margin-bottom: 2rem;
            text-align: center;
            color: #1a1a2e;
        }

        .topics-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            max-width: 1000px;
            margin: 0 auto;
        }

        .topic-item {
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .topic-icon {
            width: 50px;
            height: 50px;
            background: #0d9488;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.5rem;
        }

        .topic-item span {
            font-weight: 500;
            color: #333;
        }

        .cta-section {
            background: #0d9488;
            color: white;
            text-align: center;
            padding: 4rem 2rem;
        }

        .cta-section h2 {
            font-size: 2rem;
            margin-bottom: 1rem;
            color: white;
        }

        .cta-section p {
            font-size: 1.1rem;
            margin-bottom: 2rem;
            opacity: 0.95;
        }

        .cta-btn {
            display: inline-block;
            background: white;
            color: #0d9488;
            padding: 1rem 2.5rem;
            border-radius: 4px;
            text-decoration: none;
            font-weight: 600;
            transition: transform 0.2s;
        }

        .cta-btn:hover {
            transform: translateY(-2px);
        }

        footer {
            background: #000;
            color: white;
            padding: 3rem 2rem;
            text-align: center;
        }

        footer .links {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }

        footer a {
            color: #fff;
            text-decoration: none;
            font-size: 0.95rem;
        }

        footer a:hover {
            color: #14b8a6;
        }

        footer p {
            color: #999;
            font-size: 0.9rem;
        }

        @media (max-width: 768px) {
            .program-hero h1 {
                font-size: 2rem;
            }
            nav ul {
                gap: 1rem;
                flex-wrap: wrap;
                justify-content: center;
            }
            nav .container {
                flex-direction: column;
                gap: 1rem;
            }
            .seminars-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <nav>
        <div class="container">
            <a href="/" class="logo">
                <img src="/static/logo.svg" alt="NexYouth">
            </a>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/#what-we-do">What We Do</a></li>
                <li class="dropdown">
                    <a href="/#programs">Programs ▾</a>
                    <div class="dropdown-menu">
                        <a href="/programs/skill-development">Skill Development Courses</a>
                        <a href="/programs/seminars">Expert Seminars & Talks</a>
                        <a href="/programs/mentorship">Global Mentorship Network</a>
                        <a href="/programs/environmental-competition">Environmental Youth Competition</a>
                    </div>
                </li>
                <li><a href="/#community">Community</a></li>
                <li><a href="/partner">Partner</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <section class="program-hero">
        <div class="container">
            <h1>Expert Seminars & Talks</h1>
            <p>Learn from industry leaders, environmental experts, and successful entrepreneurs. Our seminars bring world-class knowledge directly to aspiring young changemakers.</p>
        </div>
    </section>

    <section class="program-content">
        <div class="container">
            <h2>Featured Seminars</h2>
            <p>Our expert-led seminars cover a wide range of topics designed to inspire, educate, and empower the next generation of leaders. Each session features interactive Q&A and networking opportunities.</p>

            <div class="seminars-grid">
                <div class="seminar-card">
                    <div class="seminar-card-header">
                        <h3>Climate Action Leadership</h3>
                        <span>Environmental Series</span>
                    </div>
                    <div class="seminar-card-body">
                        <p>Explore strategies for leading climate initiatives in your community. Learn from environmental activists and policy experts about making real impact.</p>
                    </div>
                </div>
                <div class="seminar-card">
                    <div class="seminar-card-header">
                        <h3>Youth Entrepreneurship</h3>
                        <span>Business Series</span>
                    </div>
                    <div class="seminar-card-body">
                        <p>Discover how young entrepreneurs are building successful ventures. Get practical advice on ideation, funding, and scaling your ideas.</p>
                    </div>
                </div>
                <div class="seminar-card">
                    <div class="seminar-card-header">
                        <h3>Tech for Good</h3>
                        <span>Innovation Series</span>
                    </div>
                    <div class="seminar-card-body">
                        <p>Learn how technology can be leveraged to solve social and environmental challenges. Hear from tech leaders making a difference.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="topics-section">
        <div class="container">
            <h2>Topics We Cover</h2>
            <div class="topics-list">
                <div class="topic-item">
                    <div class="topic-icon">🌍</div>
                    <span>Sustainability & Climate</span>
                </div>
                <div class="topic-item">
                    <div class="topic-icon">💡</div>
                    <span>Innovation & Technology</span>
                </div>
                <div class="topic-item">
                    <div class="topic-icon">🎯</div>
                    <span>Leadership & Strategy</span>
                </div>
                <div class="topic-item">
                    <div class="topic-icon">📢</div>
                    <span>Advocacy & Communication</span>
                </div>
                <div class="topic-item">
                    <div class="topic-icon">🤝</div>
                    <span>Community Building</span>
                </div>
                <div class="topic-item">
                    <div class="topic-icon">📊</div>
                    <span>Data & Research</span>
                </div>
            </div>
        </div>
    </section>

    <section class="cta-section">
        <div class="container">
            <h2>Don't Miss Our Next Seminar</h2>
            <p>Join our mailing list to get notified about upcoming expert talks and events.</p>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform?pli=1" target="_blank" class="cta-btn">Sign Up</a>
        <div class="container">
            <p>&copy; 2023 NexYouth. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

MENTORSHIP_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Global Mentorship Network - NexYouth</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #fff;
        }

        nav {
            background: white;
            border-bottom: 1px solid #eee;
            position: sticky;
            top: 0;
            z-index: 50;
            padding: 0.8rem 2rem;
        }

        nav .container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        nav .logo {
            display: flex;
            align-items: center;
            text-decoration: none;
        }

        nav .logo img {
            height: 70px;
            width: auto;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        nav ul li {
            position: relative;
        }

        nav a {
            text-decoration: none;
            color: #333;
            font-size: 1rem;
            font-weight: 500;
            transition: color 0.2s;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        nav a:hover {
            color: #00d4ff;
        }

        /* Dropdown Menu */
        .dropdown-menu {
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            min-width: 220px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            padding: 0.5rem 0;
            z-index: 100;
        }

        .dropdown:hover .dropdown-menu {
            display: block;
        }

        .dropdown-menu a {
            display: block;
            padding: 0.8rem 1.2rem;
            font-size: 0.9rem;
            text-transform: none;
            letter-spacing: 0;
            color: #333;
        }

        .dropdown-menu a:hover {
            background: #f5f5f5;
            color: #00d4ff;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .program-hero {
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            color: white;
            text-align: center;
            padding: 6rem 2rem;
        }

        .program-hero h1 {
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
        }

        .program-hero p {
            font-size: 1.2rem;
            max-width: 800px;
            margin: 0 auto;
            opacity: 0.95;
            line-height: 1.8;
        }

        .program-content {
            padding: 5rem 2rem;
        }

        .program-content h2 {
            font-size: 2rem;
            margin-bottom: 1.5rem;
            color: #1a1a2e;
        }

        .program-content p {
            font-size: 1.1rem;
            line-height: 1.8;
            margin-bottom: 1.5rem;
            color: #555;
        }

        .benefits-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2rem;
            margin-top: 3rem;
        }

        .benefit-card {
            background: white;
            border-radius: 12px;
            padding: 2rem;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            text-align: center;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .benefit-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
        }

        .benefit-icon {
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1.5rem;
            font-size: 2rem;
        }

        .benefit-card h3 {
            font-size: 1.3rem;
            margin-bottom: 1rem;
            color: #1a1a2e;
        }

        .benefit-card p {
            font-size: 1rem;
            color: #666;
            margin-bottom: 0;
        }

        .how-it-works {
            background: #f9f9f9;
            padding: 5rem 2rem;
        }

        .how-it-works h2 {
            font-size: 2rem;
            margin-bottom: 3rem;
            text-align: center;
            color: #1a1a2e;
        }

        .steps {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 2rem;
            max-width: 1000px;
            margin: 0 auto;
        }

        .step {
            flex: 1;
            min-width: 250px;
            text-align: center;
            position: relative;
        }

        .step-number {
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            color: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            font-weight: 700;
            margin: 0 auto 1.5rem;
        }

        .step h3 {
            font-size: 1.2rem;
            margin-bottom: 0.8rem;
            color: #1a1a2e;
        }

        .step p {
            font-size: 1rem;
            color: #666;
        }

        .cta-section {
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            color: white;
            text-align: center;
            padding: 4rem 2rem;
        }

        .cta-section h2 {
            font-size: 2rem;
            margin-bottom: 1rem;
            color: white;
        }

        .cta-section p {
            font-size: 1.1rem;
            margin-bottom: 2rem;
            opacity: 0.95;
        }

        .cta-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
        }

        .cta-btn {
            display: inline-block;
            background: white;
            color: #6366f1;
            padding: 1rem 2.5rem;
            border-radius: 4px;
            text-decoration: none;
            font-weight: 600;
            transition: transform 0.2s;
        }

        .cta-btn.secondary {
            background: transparent;
            border: 2px solid white;
            color: white;
        }

        .cta-btn:hover {
            transform: translateY(-2px);
        }

        footer {
            background: #000;
            color: white;
            padding: 3rem 2rem;
            text-align: center;
        }

        footer .links {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }

        footer a {
            color: #fff;
            text-decoration: none;
            font-size: 0.95rem;
        }

        footer a:hover {
            color: #8b5cf6;
        }

        footer p {
            color: #999;
            font-size: 0.9rem;
        }

        @media (max-width: 768px) {
            .program-hero h1 {
                font-size: 2rem;
            }
            nav ul {
                gap: 1rem;
                flex-wrap: wrap;
                justify-content: center;
            }
            nav .container {
                flex-direction: column;
                gap: 1rem;
            }
        }
    </style>
</head>
<body>
    <nav>
        <div class="container">
            <a href="/" class="logo">
                <img src="/static/logo.svg" alt="NexYouth">
            </a>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/#what-we-do">What We Do</a></li>
                <li class="dropdown">
                    <a href="/#programs">Programs ▾</a>
                    <div class="dropdown-menu">
                        <a href="/programs/skill-development">Skill Development Courses</a>
                        <a href="/programs/seminars">Expert Seminars & Talks</a>
                        <a href="/programs/mentorship">Global Mentorship Network</a>
                        <a href="/programs/environmental-competition">Environmental Youth Competition</a>
                    </div>
                </li>
                <li><a href="/#community">Community</a></li>
                <li><a href="/partner">Partner</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <section class="program-hero">
        <div class="container">
            <h1>Global Mentorship Network</h1>
            <p>Connect with experienced mentors from around the world who are passionate about guiding the next generation of leaders and changemakers.</p>
        </div>
    </section>

    <section class="program-content">
        <div class="container">
            <h2>Why Mentorship Matters</h2>
            <p>Our Global Mentorship Network pairs young leaders with experienced professionals who can provide guidance, support, and real-world insights. Whether you're exploring career paths, working on a project, or developing leadership skills, our mentors are here to help you succeed.</p>

            <div class="benefits-grid">
                <div class="benefit-card">
                    <div class="benefit-icon">🎯</div>
                    <h3>Personalized Guidance</h3>
                    <p>Get one-on-one support tailored to your unique goals and challenges from mentors who have been in your shoes.</p>
                </div>
                <div class="benefit-card">
                    <div class="benefit-icon">🌐</div>
                    <h3>Global Perspectives</h3>
                    <p>Connect with mentors from diverse backgrounds and industries across different countries and cultures.</p>
                </div>
                <div class="benefit-card">
                    <div class="benefit-icon">🚀</div>
                    <h3>Career Development</h3>
                    <p>Gain insights into various career paths and develop skills that will set you apart in your future endeavors.</p>
                </div>
                <div class="benefit-card">
                    <div class="benefit-icon">🤝</div>
                    <h3>Lasting Connections</h3>
                    <p>Build meaningful relationships that extend beyond the program and become part of a supportive network.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="how-it-works">
        <div class="container">
            <h2>How It Works</h2>
            <div class="steps">
                <div class="step">
                    <div class="step-number">1</div>
                    <h3>Apply</h3>
                    <p>Fill out our application form telling us about your goals and what you're looking for in a mentor.</p>
                </div>
                <div class="step">
                    <div class="step-number">2</div>
                    <h3>Get Matched</h3>
                    <p>Our team carefully matches you with a mentor based on your interests, goals, and background.</p>
                </div>
                <div class="step">
                    <div class="step-number">3</div>
                    <h3>Connect</h3>
                    <p>Meet with your mentor regularly via video calls, work on projects together, and grow.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="cta-section">
        <div class="container">
            <h2>Ready to Get Started?</h2>
            <p>Whether you want to be a mentee or share your experience as a mentor, we'd love to hear from you.</p>
            <div class="cta-buttons">
                <a href="https://forms.gle/YxCWJ32dZJTofHREA" target="_blank" class="cta-btn">Find a Mentor</a>
                <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform?pli=1" target="_blank" class="cta-btn secondary">Become a Mentor</a>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2023 NexYouth. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

# Program Routes
@app.route('/programs/skill-development')
def skill_development():
    return render_template('skill-development.html')

@app.route('/programs/seminars')
def seminars():
    return render_template('seminars.html')

@app.route('/programs/mentorship')
def mentorship():
    return render_template('mentorship.html')

@app.route('/programs/environmental-competition')
def environmental_competition():
    return render_template('environmental-competition.html')

# Partner Page Template
ENVIRONMENTAL_COMPETITION_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>International Youth Environmental Competition - NexYouth</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #fff;
        }

        nav {
            background: white;
            border-bottom: 1px solid #eee;
            position: sticky;
            top: 0;
            z-index: 50;
            padding: 0.8rem 2rem;
        }

        nav .container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        nav .logo {
            display: flex;
            align-items: center;
            text-decoration: none;
        }

        nav .logo img {
            height: 70px;
            width: auto;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        nav ul li {
            position: relative;
        }

        nav a {
            text-decoration: none;
            color: #333;
            font-size: 1rem;
            font-weight: 500;
            transition: color 0.2s;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        nav a:hover {
            color: #00d4ff;
        }

        /* Dropdown Menu */
        .dropdown-menu {
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            min-width: 220px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            padding: 0.5rem 0;
            z-index: 100;
        }

        .dropdown:hover .dropdown-menu {
            display: block;
        }

        .dropdown-menu a {
            display: block;
            padding: 0.8rem 1.2rem;
            font-size: 0.9rem;
            text-transform: none;
            letter-spacing: 0;
            color: #333;
        }

        .dropdown-menu a:hover {
            background: #f5f5f5;
            color: #00d4ff;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .program-hero {
            background: linear-gradient(135deg, #059669 0%, #10b981 100%);
            color: white;
            text-align: center;
            padding: 6rem 2rem;
        }

        .program-hero h1 {
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
        }

        .program-hero p {
            font-size: 1.2rem;
            max-width: 800px;
            margin: 0 auto;
            opacity: 0.95;
            line-height: 1.8;
        }

        .program-content {
            padding: 5rem 2rem;
        }

        .program-content h2 {
            font-size: 2rem;
            margin-bottom: 1.5rem;
            color: #1a1a2e;
        }

        .program-content p {
            font-size: 1.1rem;
            line-height: 1.8;
            margin-bottom: 1.5rem;
            color: #555;
        }

        .competition-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .competition-card {
            background: white;
            border-radius: 12px;
            padding: 2rem;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            text-align: center;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .competition-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
        }

        .competition-icon {
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #059669 0%, #10b981 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1.5rem;
            font-size: 2rem;
        }

        .competition-card h3 {
            font-size: 1.3rem;
            margin-bottom: 1rem;
            color: #1a1a2e;
        }

        .competition-card p {
            font-size: 1rem;
            color: #666;
            margin-bottom: 0;
        }

        .themes-section {
            background: #f9f9f9;
            padding: 5rem 2rem;
        }

        .themes-section h2 {
            font-size: 2rem;
            margin-bottom: 2rem;
            text-align: center;
            color: #1a1a2e;
        }

        .themes-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            max-width: 1000px;
            margin: 0 auto;
        }

        .theme-item {
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            text-align: center;
        }

        .theme-item span {
            font-weight: 500;
            color: #333;
        }

        .details-section {
            padding: 5rem 2rem;
        }

        .details-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .detail-card {
            background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
            border-radius: 12px;
            padding: 2rem;
            border-left: 4px solid #059669;
        }

        .detail-card h3 {
            font-size: 1.2rem;
            color: #059669;
            margin-bottom: 0.8rem;
        }

        .detail-card p {
            font-size: 1rem;
            color: #555;
            margin-bottom: 0;
        }

        .prizes-section {
            background: linear-gradient(135deg, #059669 0%, #10b981 100%);
            color: white;
            padding: 5rem 2rem;
        }

        .prizes-section h2 {
            font-size: 2rem;
            margin-bottom: 2rem;
            text-align: center;
            color: white;
        }

        .prizes-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            max-width: 900px;
            margin: 0 auto;
        }

        .prize-card {
            background: rgba(255, 255, 255, 0.1);
            border: 2px solid rgba(255, 255, 255, 0.2);
            padding: 2rem;
            border-radius: 12px;
            text-align: center;
        }

        .prize-card h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }

        .prize-card p {
            font-size: 1.1rem;
            margin-bottom: 0;
        }

        .cta-section {
            background: #059669;
            color: white;
            text-align: center;
            padding: 4rem 2rem;
        }

        .cta-section h2 {
            font-size: 2rem;
            margin-bottom: 1rem;
            color: white;
        }

        .cta-section p {
            font-size: 1.1rem;
            margin-bottom: 2rem;
            opacity: 0.95;
        }

        .cta-btn {
            display: inline-block;
            background: white;
            color: #059669;
            padding: 1rem 2.5rem;
            border-radius: 4px;
            text-decoration: none;
            font-weight: 600;
            transition: transform 0.2s;
        }

        .cta-btn:hover {
            transform: translateY(-2px);
        }

        footer {
            background: #000;
            color: white;
            padding: 3rem 2rem;
            text-align: center;
        }

        footer .links {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }

        footer a {
            color: #fff;
            text-decoration: none;
            font-size: 0.95rem;
        }

        footer a:hover {
            color: #10b981;
        }

        footer p {
            color: #999;
            font-size: 0.9rem;
        }

        .winner-card {
            background: white;
            border-radius: 12px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            border-left: 5px solid #059669;
            display: flex;
            gap: 2rem;
            align-items: flex-start;
        }

        .winner-image {
            flex-shrink: 0;
            width: 140px;
            height: 140px;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .winner-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .winner-info {
            flex-grow: 1;
        }

        .avatar {
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            font-weight: 700;
            color: white;
            border-radius: 8px;
        }

        .avatar-as { background: linear-gradient(135deg, #0891b2 0%, #06b6d4 100%); }
        .avatar-nat { background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%); }
        .avatar-as2 { background: linear-gradient(135deg, #dc2626 0%, #f87171 100%); }
        .avatar-gst { background: linear-gradient(135deg, #ea580c 0%, #fb923c 100%); }
        .avatar-ry { background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%); }
        .avatar-sw { background: linear-gradient(135deg, #059669 0%, #10b981 100%); }
        .avatar-jj { background: linear-gradient(135deg, #0ea5e9 0%, #06b6d4 100%); }
        .avatar-jj2 { background: linear-gradient(135deg, #8b5cf6 0%, #a78bfa 100%); }
        .avatar-xj { background: linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%); }
        .avatar-ak { background: linear-gradient(135deg, #ec4899 0%, #f472b6 100%); }
        .avatar-ec { background: linear-gradient(135deg, #14b8a6 0%, #2dd4bf 100%); }
        .avatar-wz { background: linear-gradient(135deg, #06b6d4 0%, #22d3ee 100%); }
        .avatar-sh { background: linear-gradient(135deg, #a78bfa 0%, #c4b5fd 100%); }

        @media (max-width: 768px) {
            .program-hero h1 {
                font-size: 2rem;
            }
            nav ul {
                gap: 1rem;
                flex-wrap: wrap;
                justify-content: center;
            }
            nav .container {
                flex-direction: column;
                gap: 1rem;
            }
            .winner-card {
                flex-direction: column;
                align-items: center;
                text-align: center;
            }
            .winner-image {
                width: 120px;
                height: 120px;
            }
        }
    </style>
</head>
<body>
    <nav>
        <div class="container">
            <a href="/" class="logo">
                <img src="/static/logo.svg" alt="NexYouth">
            </a>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/#what-we-do">What We Do</a></li>
                <li class="dropdown">
                    <a href="/#programs">Programs ▾</a>
                    <div class="dropdown-menu">
                        <a href="/programs/skill-development">Skill Development Courses</a>
                        <a href="/programs/seminars">Expert Seminars & Talks</a>
                        <a href="/programs/mentorship">Global Mentorship Network</a>
                        <a href="/programs/environmental-competition">Environmental Youth Competition</a>
                    </div>
                </li>
                <li><a href="/#community">Community</a></li>
                <li><a href="/partner">Partner</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <section class="program-hero">
        <div class="container">
            <h1>🌍 International Youth Environmental Competition</h1>
            <p>Inspire. Innovate. Impact. Submit your environmental solution and compete globally with young changemakers from around the world.</p>
        </div>
    </section>

    <section class="program-content">
        <div class="container">
            <h2>About the IYEC</h2>
            <p>The International Youth Environmental Competition (IYEC) is an annual event dedicated to inspiring and empowering youth to take action on environmental and climate issues. This competition unites passionate young innovators from around the world to share ideas and projects addressing local environmental challenges with effective solutions.</p>

            <div class="competition-grid">
                <div class="competition-card">
                    <div class="competition-icon">👥</div>
                    <h3>For Youth Ages 13-18</h3>
                    <p>Open to students and young activists from all backgrounds and experience levels worldwide.</p>
                </div>
                <div class="competition-card">
                    <div class="competition-icon">📝</div>
                    <h3>Multiple Formats</h3>
                    <p>Submit essays (500-1000 words), videos (1-5 minutes), speeches, or other creative formats.</p>
                </div>
                <div class="competition-card">
                    <div class="competition-icon">💰</div>
                    <h3>Win Scholarships</h3>
                    <p>1st place: $200 | 2nd place: $150 | Junior Award: $100</p>
                </div>
            </div>
        </div>
    </section>

    <section class="themes-section">
        <div class="container">
            <h2>Competition Themes</h2>
            <p style="text-align: center; margin-bottom: 2rem; color: #666;">Pick a local issue related to one of these themes:</p>
            <div class="themes-grid">
                <div class="theme-item">
                    <span>🍃 Nature & Protection</span>
                </div>
                <div class="theme-item">
                    <span>💨 Air Quality</span>
                </div>
                <div class="theme-item">
                    <span>💧 Water & Ecosystems</span>
                </div>
                <div class="theme-item">
                    <span>♻️ Waste Management</span>
                </div>
                <div class="theme-item">
                    <span>🌡️ Climate Change</span>
                </div>
            </div>
        </div>
    </section>

    <section class="prizes-section">
        <div class="container">
            <h2 style="color: white;">🏆 Awards</h2>
            <div class="prizes-grid">
                <div class="prize-card">
                    <h3>🥇 1st Place</h3>
                    <p>$200 Scholarship</p>
                </div>
                <div class="prize-card">
                    <h3>🥈 2nd Place</h3>
                    <p>$150 Scholarship</p>
                </div>
                <div class="prize-card">
                    <h3>⭐ Ingenuity Award</h3>
                    <p>$100 Scholarship</p>
                </div>
            </div>
        </div>
    </section>

    <section class="details-section">
        <div class="container">
            <h2>How to Participate</h2>
            <div class="details-grid">
                <div class="detail-card">
                    <h3>1️⃣ Prepare Your Project</h3>
                    <p>Develop an innovative solution to a local environmental issue. No prior experience needed—focus on creativity and practical impact.</p>
                </div>
                <div class="detail-card">
                    <h3>2️⃣ Choose Your Format</h3>
                    <p>Present as an essay, video, speech, or creative format. Make sure it's in English or has English subtitles.</p>
                </div>
                <div class="detail-card">
                    <h3>3️⃣ Submit Online</h3>
                    <p>Fill out the submission form with your project details. Submission deadline: January 15, 2026.</p>
                </div>
            </div>
        </div>
    </section>



    <section style="background: #f9f9f9; padding: 5rem 2rem;">
        <div class="container">
            <h2 style="font-size: 2rem; margin-bottom: 2rem; color: #1a1a2e;">Past Award Winners</h2>
            
            <div style="margin-bottom: 4rem;">
                <h3 style="font-size: 1.5rem; color: #059669; margin-bottom: 2rem; border-bottom: 3px solid #059669; padding-bottom: 1rem;">🏆 2024-2025 Senior Category Winners</h3>
                
                <div class="winner-card">
                    <div class="winner-image">
                        <div class="avatar avatar-as">AS</div>
                    </div>
                    <div class="winner-info">
                        <h4 style="color: #059669; font-size: 1.3rem; margin-bottom: 0.5rem;">🥇 1st Place: Amanullah Solangi</h4>
                        <p style="color: #888; font-size: 0.95rem; margin-bottom: 1rem;"><strong>Government Degree College, Matiari • Hyderabad, Sindh, Pakistan</strong></p>
                        <p style="color: #333; font-size: 1rem; margin-bottom: 1rem;"><strong>Project: "Cool Hyderabad: A Green Initiative to Combat Urban Heat and Climate Change"</strong></p>
                        <p style="color: #666; line-height: 1.8;">Cool Hyderabad is an eco-friendly initiative led by youth to address urban heat and climate change through mass tree plantations in Hyderabad. By planting 100,000 trees and involving the community, the project promotes sustainability, improves air quality, and raises environmental awareness among students, volunteers, and the general public.</p>
                    </div>
                </div>

                <div class="winner-card">
                    <div class="winner-image">
                        <div class="avatar avatar-nat">NAT</div>
                    </div>
                    <div class="winner-info">
                        <h4 style="color: #059669; font-size: 1.3rem; margin-bottom: 0.5rem;">🥈 2nd Place: Ngô Anh Tuấn & Duong Hai Mien</h4>
                        <p style="color: #888; font-size: 0.95rem; margin-bottom: 1rem;"><strong>Nguyen Trai High School & Quy Don High School for the Gifted • Da Nang, Vietnam</strong></p>
                        <p style="color: #333; font-size: 1rem; margin-bottom: 1rem;"><strong>Project: "Turning the Tides: Restoring Coastal Paradise from Pollution's Grip"</strong></p>
                        <p style="color: #666; line-height: 1.8;">Da Nang's breathtaking beaches face serious environmental threats such as plastic waste and marine pollution. Microplastics are devastating marine life and contaminating seafood. By adopting sound environmental practices, improving waste management, restoring original habitats, and rallying communities to action, the team is working to save Da Nang's natural beauty and its essence.</p>
                    </div>
                </div>

                <div style="background: white; border-radius: 12px; padding: 2rem; margin-bottom: 2rem; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08); border-left: 5px solid #d4d4d8;">
                    <h4 style="color: #78716c; font-size: 1.3rem; margin-bottom: 0.5rem;">🌟 Honorable Mention: Chun-Shan CHANG</h4>
                    <p style="color: #888; font-size: 0.95rem; margin-bottom: 1rem;"><strong>Kang Chiao International School • New Taipei City, Taiwan</strong></p>
                    <p style="color: #333; font-size: 1rem; margin-bottom: 1rem;"><strong>Project: "The Inconsistent Perception Between Travel Experience and Environmental Awareness"</strong></p>
                    <p style="color: #666; line-height: 1.8;">Exploring Taiwan's 2025 regulation banning disposable plastic amenities in hotels and B&Bs, this project examines public perceptions of environmental protection versus hospitality expectations, aiming to find a balance between sustainability and guest experience.</p>
                </div>
            </div>

            <div style="margin-bottom: 4rem;">
                <h3 style="font-size: 1.5rem; color: #059669; margin-bottom: 2rem; border-bottom: 3px solid #059669; padding-bottom: 1rem;">⭐ 2024-2025 IYEC Ingenuity Award</h3>
                
                <div class="winner-card">
                    <div class="winner-image">
                        <div class="avatar avatar-as2">AS</div>
                    </div>
                    <div class="winner-info">
                        <h4 style="color: #059669; font-size: 1.3rem; margin-bottom: 0.5rem;">🚀 Atharva Soni, Arav Kamat, Sadik Premjee & Aria Kamat</h4>
                        <p style="color: #888; font-size: 0.95rem; margin-bottom: 1rem;"><strong>Northwood High School • Irvine, California, USA</strong></p>
                        <p style="color: #333; font-size: 1rem; margin-bottom: 1rem;"><strong>Project: "Earth Z- Wildfire Solutions"</strong></p>
                        <p style="color: #666; line-height: 1.8;">Earth Z develops an AI system backed by real past and current data to detect areas of high fire risk, using datasets from NOAA and other sources. The team collected their own machine learning data to train the model, ensuring accuracy by correlating inputs with confirmed fire incidents.</p>
                    </div>
                </div>
            </div>

            <div style="margin-bottom: 4rem;">
                <h3 style="font-size: 1.5rem; color: #059669; margin-bottom: 2rem; border-bottom: 3px solid #059669; padding-bottom: 1rem;">🏆 2023-2024 Senior Category Winners</h3>
                
                <div class="winner-card">
                    <div class="winner-image">
                        <div class="avatar avatar-jw">JW</div>
                    </div>
                    <div class="winner-info">
                        <h4 style="color: #059669; font-size: 1.3rem; margin-bottom: 0.5rem;">🥇 1st Place: Joshua Waweru</h4>
                        <p style="color: #888; font-size: 0.95rem; margin-bottom: 1rem;"><strong>Starehe Boys' Centre and School • Nairobi, Kenya</strong></p>
                        <p style="color: #333; font-size: 1rem; margin-bottom: 1rem;"><strong>Project: "Youth for Sustainable Development"</strong></p>
                        <p style="color: #666; line-height: 1.8;">Joshua's project focuses on mobilizing youth communities to implement sustainable development practices in Kenya, addressing environmental challenges through education, community engagement, and practical conservation efforts that have made a measurable impact on local ecosystems.</p>
                    </div>
                </div>

                <div class="winner-card">
                    <div class="winner-image">
                        <div class="avatar avatar-sv">SV</div>
                    </div>
                    <div class="winner-info">
                        <h4 style="color: #059669; font-size: 1.3rem; margin-bottom: 0.5rem;">🥈 2nd Place: Sofia Vargas</h4>
                        <p style="color: #888; font-size: 0.95rem; margin-bottom: 1rem;"><strong>Liceo Nacional de Costa Rica • San José, Costa Rica</strong></p>
                        <p style="color: #333; font-size: 1rem; margin-bottom: 1rem;"><strong>Project: "Ocean Guardian Initiative"</strong></p>
                        <p style="color: #666; line-height: 1.8;">Sofia's initiative focuses on protecting Costa Rica's marine ecosystems through education campaigns, beach cleanups, and advocacy for sustainable fishing practices. Her work has inspired thousands of youth to take action against ocean pollution and protect endangered marine species.</p>
                    </div>
                </div>

                <div class="winner-card">
                    <div class="winner-image">
                        <div class="avatar avatar-ac">AC</div>
                    </div>
                    <div class="winner-info">
                        <h4 style="color: #059669; font-size: 1.3rem; margin-bottom: 0.5rem;">🥉 3rd Place: Aisha Chen</h4>
                        <p style="color: #888; font-size: 0.95rem; margin-bottom: 1rem;"><strong>Huayang High School • Shanghai, China</strong></p>
                        <p style="color: #333; font-size: 1rem; margin-bottom: 1rem;"><strong>Project: "Urban Green Spaces for Climate Resilience"</strong></p>
                        <p style="color: #666; line-height: 1.8;">Aisha's project creates urban green spaces in Shanghai to combat climate change and improve air quality. Through strategic planting and community involvement, she has transformed concrete areas into thriving ecosystems that provide both environmental and social benefits to local communities.</p>
                    </div>
                </div>
            </div>
            <div>
                <h3 style="font-size: 1.5rem; color: #059669; margin-bottom: 2rem; border-bottom: 3px solid #059669; padding-bottom: 1rem;">👥 2024-2025 Junior Category Winners</h3>
                
                <div class="winner-card">
                    <div class="winner-image">
                        <div class="avatar avatar-gst">GS</div>
                    </div>
                    <div class="winner-info">
                        <h4 style="color: #059669; font-size: 1.3rem; margin-bottom: 0.5rem;">🥇 1st Place: Girl Scout Troop 436</h4>
                        <p style="color: #888; font-size: 0.95rem; margin-bottom: 1rem;"><strong>Sylvie Wailand, Emily Brubaker, Adalyn Waldren, Annabelle Slinker, Mackenzie Elliott, Charlotte Nelson • Alaska, USA</strong></p>
                        <p style="color: #333; font-size: 1rem; margin-bottom: 1rem;"><strong>Project: "The BioGlitter Initiative"</strong></p>
                        <p style="color: #666; line-height: 1.8;">Girl Scout Troop 436 created the BioGlitter Initiative to raise awareness about the dangers of plastic glitter and promote biodegradable alternatives. Through education, advocacy, and creative projects, they aim to eliminate plastic glitter in Anchorage schools and the entire state of Alaska, protecting both human health and the environment from the harmful effects of microplastics.</p>
                    </div>
                </div>

                <div class="winner-card">
                    <div class="winner-image">
                        <div class="avatar avatar-ry">RY</div>
                    </div>
                    <div class="winner-info">
                        <h4 style="color: #059669; font-size: 1.3rem; margin-bottom: 0.5rem;">🥈 2nd Place: Rui-Tong Yuan</h4>
                        <p style="color: #888; font-size: 0.95rem; margin-bottom: 1rem;"><strong>Shanghai American School • Puxi, Shanghai, China</strong></p>
                        <p style="color: #333; font-size: 1rem; margin-bottom: 1rem;"><strong>Project: "Building a Better Future for All Beings: Addressing Environmental Degradation in Construction"</strong></p>
                        <p style="color: #666; line-height: 1.8;">This project explores the harms caused by unsustainable construction on humans, animals, and communities, and presents a range of solutions to help mitigate these effects and promote more sustainable development practices.</p>
                    </div>
                </div>
            </div>

            <div style="margin-bottom: 4rem;">
                <h3 style="font-size: 1.5rem; color: #059669; margin-bottom: 2rem; border-bottom: 3px solid #059669; padding-bottom: 1rem;">🏆 2023-2024 Senior Category Winners</h3>
                
                <div class="winner-card">
                    <div class="winner-image">
                        <div class="avatar avatar-jj">JJ</div>
                    </div>
                    <div class="winner-info">
                        <h4 style="color: #059669; font-size: 1.3rem; margin-bottom: 0.5rem;">🥇 1st Place: Julie Jin</h4>
                        <p style="color: #888; font-size: 0.95rem; margin-bottom: 1rem;"><strong>Colonel By Secondary School • Ottawa, Canada</strong></p>
                        <p style="color: #333; font-size: 1rem; margin-bottom: 1rem;"><strong>Project: "Become a Biodiversity Hero – From the Comfort of Home and on the Road"</strong></p>
                        <p style="color: #666; line-height: 1.8;">An innovative approach to engaging citizens in biodiversity conservation through accessible citizen science and environmental action, enabling individuals to make a real difference from their home or while traveling.</p>
                    </div>
                </div>

                <div class="winner-card">
                    <div class="winner-image">
                        <div class="avatar avatar-jj2">JJ</div>
                    </div>
                    <div class="winner-info">
                        <h4 style="color: #059669; font-size: 1.3rem; margin-bottom: 0.5rem;">🥈 2nd Place: Jenny Jin</h4>
                        <p style="color: #888; font-size: 0.95rem; margin-bottom: 1rem;"><strong>Colonel By Secondary School • Ottawa, Canada</strong></p>
                        <p style="color: #333; font-size: 1rem; margin-bottom: 1rem;"><strong>Project: "From Waste to Well-being: Managing the Global Waste Crisis"</strong></p>
                        <p style="color: #666; line-height: 1.8;">A comprehensive examination of the global waste management crisis and innovative solutions to transform waste into valuable resources, promoting circular economy principles and environmental well-being.</p>
                    </div>
                </div>

                <div style="background: white; border-radius: 12px; padding: 2rem; margin-bottom: 2rem; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08); border-left: 5px solid #d4d4d8;">
                    <h4 style="color: #78716c; font-size: 1.3rem; margin-bottom: 0.5rem;">🌟 Honorable Mention: William Zeng</h4>
                    <p style="color: #888; font-size: 0.95rem; margin-bottom: 1rem;"><strong>St Stephens School • Rome, Italy</strong></p>
                    <p style="color: #333; font-size: 1rem; margin-bottom: 1rem;"><strong>Project: "Rome's Waste Management Crisis"</strong></p>
                    <p style="color: #666; line-height: 1.8;">Proposed solutions include anaerobic digestion for organic waste, circular economy initiatives, and localized waste-to-energy plants to reduce reliance on waste exports. These approaches aim to foster a sustainable system, preparing the city for the upcoming Jubilee Year.</p>
                </div>
            </div>

            <div style="margin-bottom: 4rem;">
                <h3 style="font-size: 1.5rem; color: #059669; margin-bottom: 2rem; border-bottom: 3px solid #059669; padding-bottom: 1rem;">⭐ 2023-2024 IYEC Ingenuity Award</h3>
                
                <div class="winner-card">
                    <div class="winner-image">
                        <div class="avatar avatar-xj">XJ</div>
                    </div>
                    <div class="winner-info">
                        <h4 style="color: #059669; font-size: 1.3rem; margin-bottom: 0.5rem;">🚀 Xunhao Jiang</h4>
                        <p style="color: #888; font-size: 0.95rem; margin-bottom: 1rem;"><strong>The Fifth Secondary School of Heilongjiang • Heilongjiang, China</strong></p>
                        <p style="color: #333; font-size: 1rem; margin-bottom: 1rem;"><strong>Project: "Strategies of Mitigating Pollution"</strong></p>
                        <p style="color: #666; line-height: 1.8;">An innovative examination of pollution mitigation strategies addressing multiple environmental challenges through practical and scalable solutions for implementation.</p>
                    </div>
                </div>
            </div>

            <div style="margin-bottom: 4rem;">
                <h3 style="font-size: 1.5rem; color: #059669; margin-bottom: 2rem; border-bottom: 3px solid #059669; padding-bottom: 1rem;">👥 2023-2024 Junior Category Winners</h3>
                
                <div class="winner-card">
                    <div class="winner-image">
                        <div class="avatar avatar-ak">AK</div>
                    </div>
                    <div class="winner-info">
                        <h4 style="color: #059669; font-size: 1.3rem; margin-bottom: 0.5rem;">🥇 1st Place: Alisa Jiang & Katherine Jiang</h4>
                        <p style="color: #888; font-size: 0.95rem; margin-bottom: 1rem;"><strong>Oakridge Middle School & Mason Classical Academy • Naples, Florida, USA</strong></p>
                        <p style="color: #333; font-size: 1rem; margin-bottom: 1rem;"><strong>Project: "Southwest Florida Environmental Issues"</strong></p>
                        <p style="color: #666; line-height: 1.8;">A detailed analysis of the unique environmental challenges facing Southwest Florida, examining local issues and proposing actionable solutions for regional sustainability.</p>
                    </div>
                </div>

                <div class="winner-card">
                    <div class="winner-image">
                        <div class="avatar avatar-ec">EC</div>
                    </div>
                    <div class="winner-info">
                        <h4 style="color: #059669; font-size: 1.3rem; margin-bottom: 0.5rem;">🥈 2nd Place: Even Chen</h4>
                        <p style="color: #888; font-size: 0.95rem; margin-bottom: 1rem;"><strong>Shanghai United International School • Shanghai, China</strong></p>
                        <p style="color: #333; font-size: 1rem; margin-bottom: 1rem;"><strong>Project: "A Spotlight on Local Actions that are Helping the Environment"</strong></p>
                        <p style="color: #666; line-height: 1.8;">A compelling showcase of grassroots environmental initiatives and local community actions making a positive impact, highlighting how individuals and communities can drive environmental change.</p>
                    </div>
                </div>

                <div style="background: white; border-radius: 12px; padding: 2rem; margin-bottom: 2rem; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08); border-left: 5px solid #d4d4d8;">
                    <h4 style="color: #78716c; font-size: 1.3rem; margin-bottom: 0.5rem;">🌟 Honorable Mention: Syuan-Hao HUANG</h4>
                    <p style="color: #888; font-size: 0.95rem; margin-bottom: 1rem;"><strong>Kang Chiao International School • New Taipei City, Taiwan</strong></p>
                    <p style="color: #333; font-size: 1rem; margin-bottom: 1rem;"><strong>Project: "The Tug-of-War Between Environmental Preservation and Local Economic Benefits"</strong></p>
                    <p style="color: #666; line-height: 1.8;">Marine Protected Areas (MPAs) can boost fish populations and support tourism, but they may also threaten fishers' livelihoods. Taiwan's MPAs, including South Penghu, face challenges such as unclear regulations, limited local engagement, and divided authority. Addressing these issues requires clear rules and unified administrative and enforcement responsibilities.</p>
                </div>
            </div>
        </div>
    </section>

    <section style="background: white; padding: 5rem 2rem; border-top: 1px solid #eee;">
        <div class="container">
            <h2 style="font-size: 2rem; margin-bottom: 2rem; text-align: center; color: #1a1a2e;">Meet Our Judges</h2>
            <p style="text-align: center; color: #666; margin-bottom: 3rem; font-size: 1.1rem;">Our judging panel consists of industry leaders, environmental experts, and accomplished innovators.</p>
            
            <div style="max-width: 600px; margin: 0 auto; background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border-radius: 12px; padding: 2.5rem; text-align: center; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08); margin-bottom: 3rem;">
                <div style="width: 120px; height: 120px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); background: linear-gradient(135deg, #059669 0%, #10b981 100%); font-size: 2.5rem; font-weight: 700; color: white;">
                    SW
                </div>
                <h3 style="font-size: 1.4rem; color: #059669; margin-bottom: 0.5rem;">Sigil Wen</h3>
                <p style="color: #666; font-size: 1rem; margin-bottom: 0; line-height: 1.8;"><strong>Industry-leading innovator, investor, and Wharton alumni</strong></p>
                <p style="color: #888; font-size: 0.95rem; margin-top: 1rem;">Our judges bring rich academic and industry backgrounds, ensuring fair evaluation of all submissions.</p>
            </div>

            <div style="margin-top: 3rem; padding-top: 3rem; border-top: 2px solid #eee;">
                <h3 style="font-size: 1.5rem; color: #059669; margin-bottom: 2rem; text-align: center;">Judging Criteria</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; max-width: 1000px; margin: 0 auto 3rem;">
                    <div style="background: rgba(5, 150, 105, 0.05); border-left: 4px solid #059669; padding: 2rem; border-radius: 8px; text-align: center;">
                        <h4 style="color: #059669; font-size: 1.2rem; margin-bottom: 0.5rem;">Innovation</h4>
                        <p style="color: #555; font-size: 0.95rem;">Originality and creativity of your idea</p>
                    </div>
                    <div style="background: rgba(5, 150, 105, 0.05); border-left: 4px solid #059669; padding: 2rem; border-radius: 8px; text-align: center;">
                        <h4 style="color: #059669; font-size: 1.2rem; margin-bottom: 0.5rem;">Impact</h4>
                        <p style="color: #555; font-size: 0.95rem;">Potential positive environmental effects</p>
                    </div>
                    <div style="background: rgba(5, 150, 105, 0.05); border-left: 4px solid #059669; padding: 2rem; border-radius: 8px; text-align: center;">
                        <h4 style="color: #059669; font-size: 1.2rem; margin-bottom: 0.5rem;">Feasibility</h4>
                        <p style="color: #555; font-size: 0.95rem;">Practicality and scalability</p>
                    </div>
                    <div style="background: rgba(5, 150, 105, 0.05); border-left: 4px solid #059669; padding: 2rem; border-radius: 8px; text-align: center;">
                        <h4 style="color: #059669; font-size: 1.2rem; margin-bottom: 0.5rem;">Presentation</h4>
                        <p style="color: #555; font-size: 0.95rem;">Clarity and effectiveness</p>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <section class="cta-section">
        <div class="container">
            <h2>Ready to Make a Difference?</h2>
            <p>Submit your environmental solution and compete with innovators from around the world.</p>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSc487tftJjAfLNuFsVuFODGCr7ljV-8DFdXyx9Lb5Szlxv24w/viewform?usp=sf_link" target="_blank" class="cta-btn">Submit Your Project</a>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2025 NexYouth & IYEC. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

# Partner Page Template
PARTNER_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Partner With Us - NexYouth</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #fff;
        }

        nav {
            background: white;
            border-bottom: 1px solid #eee;
            position: sticky;
            top: 0;
            z-index: 50;
            padding: 0.8rem 2rem;
        }

        nav .container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        nav .logo {
            display: flex;
            align-items: center;
            text-decoration: none;
        }

        nav .logo img {
            height: 70px;
            width: auto;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        nav ul li {
            position: relative;
        }

        nav a {
            text-decoration: none;
            color: #333;
            font-size: 1rem;
            font-weight: 500;
            transition: color 0.2s;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        nav a:hover {
            color: #00d4ff;
        }

        /* Dropdown Menu */
        .dropdown-menu {
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            min-width: 220px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            padding: 0.5rem 0;
            z-index: 100;
        }

        .dropdown:hover .dropdown-menu {
            display: block;
        }

        .dropdown-menu a {
            display: block;
            padding: 0.8rem 1.2rem;
            font-size: 0.9rem;
            text-transform: none;
            letter-spacing: 0;
            color: #333;
        }

        .dropdown-menu a:hover {
            background: #f5f5f5;
            color: #00d4ff;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .partner-hero {
            background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #0d2137 100%);
            color: white;
            text-align: center;
            padding: 8rem 2rem;
            position: relative;
            overflow: hidden;
        }

        .partner-hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 30% 20%, rgba(0, 212, 255, 0.15) 0%, transparent 50%),
                        radial-gradient(circle at 70% 80%, rgba(255, 107, 53, 0.1) 0%, transparent 50%);
            pointer-events: none;
        }

        .partner-hero .container {
            position: relative;
            z-index: 1;
        }

        .partner-hero-badge {
            display: inline-block;
            background: rgba(0, 212, 255, 0.2);
            color: #00d4ff;
            padding: 0.5rem 1.5rem;
            border-radius: 30px;
            font-size: 0.9rem;
            font-weight: 600;
            letter-spacing: 1px;
            text-transform: uppercase;
            margin-bottom: 1.5rem;
            border: 1px solid rgba(0, 212, 255, 0.3);
        }

        .partner-hero h1 {
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            line-height: 1.2;
        }

        .partner-hero h1 span {
            background: linear-gradient(135deg, #00d4ff 0%, #00a8cc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .partner-hero p {
            font-size: 1.3rem;
            max-width: 700px;
            margin: 0 auto 2.5rem;
            opacity: 0.9;
            line-height: 1.8;
        }

        .hero-stats {
            display: flex;
            justify-content: center;
            gap: 4rem;
            margin-top: 3rem;
            flex-wrap: wrap;
        }

        .hero-stat {
            text-align: center;
        }

        .hero-stat-number {
            font-size: 2.5rem;
            font-weight: 800;
            color: #00d4ff;
        }

        .hero-stat-label {
            font-size: 0.95rem;
            opacity: 0.8;
            margin-top: 0.3rem;
        }

        .partner-intro {
            padding: 6rem 2rem;
            background: white;
        }

        .intro-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
        }

        .intro-content h2 {
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
            color: #1a1a2e;
            line-height: 1.3;
        }

        .intro-content p {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #555;
            margin-bottom: 1.5rem;
        }

        .intro-features {
            margin-top: 2rem;
        }

        .intro-feature {
            display: flex;
            align-items: flex-start;
            gap: 1rem;
            margin-bottom: 1.5rem;
        }

        .intro-feature-icon {
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.2rem;
            flex-shrink: 0;
        }

        .intro-feature-text h4 {
            font-size: 1.1rem;
            color: #1a1a2e;
            margin-bottom: 0.3rem;
        }

        .intro-feature-text p {
            font-size: 0.95rem;
            color: #666;
            margin: 0;
        }

        .intro-image {
            position: relative;
        }

        .intro-image-main {
            width: 100%;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
        }

        .intro-image-float {
            position: absolute;
            bottom: -30px;
            left: -30px;
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
        }

        .intro-image-float-number {
            font-size: 2rem;
            font-weight: 800;
            color: #00d4ff;
        }

        .intro-image-float-text {
            font-size: 0.9rem;
            color: #666;
        }

        .partner-types {
            background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);
            padding: 6rem 2rem;
        }

        .partner-types h2 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            text-align: center;
            color: #1a1a2e;
        }

        .partner-types > .container > p {
            text-align: center;
            color: #666;
            font-size: 1.1rem;
            max-width: 600px;
            margin: 0 auto 3rem;
        }

        .types-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .type-card {
            background: white;
            border-radius: 20px;
            padding: 2.5rem;
            text-align: center;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
            transition: all 0.4s ease;
            border: 2px solid transparent;
            position: relative;
            overflow: hidden;
        }

        .type-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #00d4ff, #0099cc);
            transform: scaleX(0);
            transition: transform 0.4s ease;
        }

        .type-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 60px rgba(0, 212, 255, 0.15);
            border-color: rgba(0, 212, 255, 0.2);
        }

        .type-card:hover::before {
            transform: scaleX(1);
        }

        .type-icon {
            width: 90px;
            height: 90px;
            background: linear-gradient(135deg, #e8f9ff 0%, #d0f0ff 100%);
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1.5rem;
            font-size: 2.5rem;
            transition: transform 0.3s ease;
        }

        .type-card:hover .type-icon {
            transform: scale(1.1) rotate(5deg);
        }

        .type-card h3 {
            font-size: 1.4rem;
            margin-bottom: 1rem;
            color: #1a1a2e;
        }

        .type-card p {
            font-size: 1rem;
            color: #666;
            line-height: 1.7;
            margin-bottom: 1.5rem;
        }

        .type-card-link {
            color: #00d4ff;
            font-weight: 600;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: gap 0.3s ease;
        }

        .type-card-link:hover {
            gap: 0.8rem;
        }

        /* Impact Numbers Section */
        .impact-section {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            padding: 5rem 2rem;
            color: white;
        }

        .impact-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2rem;
            max-width: 1000px;
            margin: 0 auto;
        }

        .impact-item {
            text-align: center;
            padding: 1.5rem;
        }

        .impact-number {
            font-size: 3rem;
            font-weight: 800;
            background: linear-gradient(135deg, #00d4ff 0%, #00a8cc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .impact-label {
            font-size: 1rem;
            opacity: 0.9;
            margin-top: 0.5rem;
        }

        .benefits-section {
            padding: 6rem 2rem;
            background: white;
        }

        .benefits-section h2 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            text-align: center;
            color: #1a1a2e;
        }

        .benefits-section > .container > p {
            text-align: center;
            color: #666;
            font-size: 1.1rem;
            max-width: 600px;
            margin: 0 auto 3rem;
        }

        .benefits-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
            max-width: 1100px;
            margin: 0 auto;
        }

        .benefit-card {
            background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
            border-radius: 16px;
            padding: 2rem;
            border: 1px solid #eee;
            transition: all 0.3s ease;
        }

        .benefit-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
            border-color: #00d4ff;
        }

        .benefit-icon {
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.5rem;
            margin-bottom: 1.5rem;
        }

        .benefit-card h3 {
            font-size: 1.2rem;
            color: #1a1a2e;
            margin-bottom: 0.8rem;
        }

        .benefit-card p {
            font-size: 0.95rem;
            color: #666;
            line-height: 1.6;
        }

        /* Current Partners Section */
        .current-partners {
            padding: 6rem 2rem;
            background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);
        }

        .current-partners h2 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            text-align: center;
            color: #1a1a2e;
        }

        .current-partners > .container > p {
            text-align: center;
            color: #666;
            margin-bottom: 3rem;
            font-size: 1.1rem;
        }

        .partners-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .partner-card {
            background: white;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
            transition: all 0.4s ease;
        }

        .partner-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.12);
        }

        .partner-card-header {
            background: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%);
            color: white;
            padding: 2rem;
            text-align: center;
        }

        .partner-card-header h3 {
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
        }

        .partner-card-header span {
            font-size: 0.9rem;
            opacity: 0.9;
            background: rgba(255,255,255,0.2);
            padding: 0.3rem 1rem;
            border-radius: 20px;
            display: inline-block;
        }

        .partner-card-body {
            padding: 2rem;
        }

        .partner-card-body h4 {
            font-size: 1.2rem;
            color: #1a1a2e;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .partner-card-body p {
            font-size: 1rem;
            color: #666;
        }

        .type-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
        }

        .type-icon {
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1.5rem;
            font-size: 2.5rem;
        }

        .type-card h3 {
            font-size: 1.4rem;
            margin-bottom: 1rem;
            color: #1a1a2e;
        }

        .type-card p {
            font-size: 1rem;
            color: #666;
            line-height: 1.7;
        }

        .benefits-section {
            padding: 5rem 2rem;
        }

        .benefits-section h2 {
            font-size: 2rem;
            margin-bottom: 3rem;
            text-align: center;
            color: #1a1a2e;
        }

        .benefits-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
            max-width: 1000px;
            margin: 0 auto;
        }

        .benefit-item {
            display: flex;
            align-items: flex-start;
            gap: 1rem;
            padding: 1.5rem;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        }

        .benefit-check {
            width: 30px;
            height: 30px;
            background: #00d4ff;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1rem;
            flex-shrink: 0;
        }

        .benefit-item span {
            font-size: 1rem;
            color: #333;
            line-height: 1.6;
        }

        /* Current Partners Section */
        .current-partners {
            padding: 5rem 2rem;
            background: #f9f9f9;
        }

        .current-partners h2 {
            font-size: 2rem;
            margin-bottom: 1rem;
            text-align: center;
            color: #1a1a2e;
        }

        .current-partners > .container > p {
            text-align: center;
            color: #666;
            margin-bottom: 3rem;
            font-size: 1.1rem;
        }

        .partners-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .partner-card {
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .partner-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
        }

        .partner-card-header {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: white;
            padding: 2rem;
            text-align: center;
        }

        .partner-card-header h3 {
            font-size: 1.4rem;
            margin-bottom: 0.5rem;
        }

        .partner-card-header span {
            font-size: 0.9rem;
            opacity: 0.9;
        }

        .partner-card-body {
            padding: 2rem;
        }

        .partner-card-body h4 {
            font-size: 1.1rem;
            color: #1a1a2e;
            margin-bottom: 0.8rem;
        }

        .partner-card-body p {
            font-size: 1rem;
            color: #666;
            line-height: 1.7;
            margin-bottom: 1rem;
        }

        .partner-video {
            margin: 1.5rem 0;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
        }

        .partner-video video {
            width: 100%;
            display: block;
        }

        .partner-tag {
            display: inline-block;
            background: linear-gradient(135deg, #e8f9ff 0%, #d0f0ff 100%);
            color: #0099cc;
            padding: 0.4rem 1rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
        }

        .cta-section {
            background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #0d2137 100%);
            color: white;
            text-align: center;
            padding: 6rem 2rem;
            position: relative;
            overflow: hidden;
        }

        .cta-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 50% 50%, rgba(0, 212, 255, 0.1) 0%, transparent 60%);
            pointer-events: none;
        }

        .cta-section .container {
            position: relative;
            z-index: 1;
        }

        .cta-section h2 {
            font-size: 2.8rem;
            margin-bottom: 1rem;
            color: white;
        }

        .cta-section h2 span {
            background: linear-gradient(135deg, #00d4ff 0%, #00a8cc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .cta-section p {
            font-size: 1.2rem;
            margin-bottom: 2.5rem;
            opacity: 0.9;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }

        .cta-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
        }

        .cta-btn {
            display: inline-block;
            background: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%);
            color: white;
            padding: 1rem 2.5rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            font-size: 1.1rem;
            transition: all 0.3s ease;
            box-shadow: 0 5px 20px rgba(0, 212, 255, 0.3);
        }

        .cta-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(0, 212, 255, 0.4);
        }

        .cta-btn.secondary {
            background: transparent;
            border: 2px solid rgba(255, 255, 255, 0.3);
            box-shadow: none;
        }

        .cta-btn.secondary:hover {
            background: rgba(255, 255, 255, 0.1);
            border-color: rgba(255, 255, 255, 0.5);
        }

        .contact-email {
            margin-top: 2rem;
            font-size: 1rem;
            opacity: 0.8;
        }

        .contact-email a {
            color: #00d4ff;
            text-decoration: none;
            font-weight: 500;
        }

        .contact-email a:hover {
            text-decoration: underline;
        }

        footer {
            background: #000;
            color: white;
            padding: 3rem 2rem;
            text-align: center;
        }

        footer .links {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }

        footer a {
            color: #fff;
            text-decoration: none;
            font-size: 0.95rem;
        }

        footer a:hover {
            color: #00d4ff;
        }

        footer p {
            color: #999;
            font-size: 0.9rem;
        }

        @media (max-width: 1024px) {
            .intro-grid {
                grid-template-columns: 1fr;
                gap: 3rem;
            }
            .types-grid, .benefits-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            .impact-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 768px) {
            .partner-hero h1 {
                font-size: 2.2rem;
            }
            .hero-stats {
                gap: 2rem;
            }
            .types-grid, .benefits-grid {
                grid-template-columns: 1fr;
            }
            .partners-grid {
                grid-template-columns: 1fr;
            }
            nav ul {
                gap: 1rem;
                flex-wrap: wrap;
                justify-content: center;
            }
            nav .container {
                flex-direction: column;
                gap: 1rem;
            }
        }
    </style>
</head>
<body>
    <nav>
        <div class="container">
            <a href="/" class="logo">
                <img src="/static/logo.svg" alt="NexYouth">
            </a>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/#what-we-do">What We Do</a></li>
                <li class="dropdown">
                    <a href="/#programs">Programs ▾</a>
                    <div class="dropdown-menu">
                        <a href="/programs/skill-development">Skill Development Courses</a>
                        <a href="/programs/seminars">Expert Seminars & Talks</a>
                        <a href="/programs/mentorship">Global Mentorship Network</a>
                        <a href="/programs/environmental-competition">Environmental Youth Competition</a>
                    </div>
                </li>
                <li><a href="/#community">Community</a></li>
                <li><a href="/partner">Partner</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <section class="partner-hero">
        <div class="container">
            <div class="partner-hero-badge">🤝 Partnership Program</div>
            <h1>Let's Create <span>Impact Together</span></h1>
            <p>Partner with NexYouth to empower the next generation of leaders. Together, we can provide youth with the skills, mentorship, and opportunities they need to succeed.</p>
            <div class="hero-stats">
                <div class="hero-stat">
                    <div class="hero-stat-number">5000+</div>
                    <div class="hero-stat-label">Youth Impacted</div>
                </div>
                <div class="hero-stat">
                    <div class="hero-stat-number">13+</div>
                    <div class="hero-stat-label">Countries</div>
                </div>
                <div class="hero-stat">
                    <div class="hero-stat-number">90+</div>
                    <div class="hero-stat-label">Schools</div>
                </div>
            </div>
        </div>
    </section>

    <section class="partner-intro">
        <div class="intro-grid">
            <div class="intro-content">
                <h2>Why Partner With NexYouth?</h2>
                <p>We're building a global movement of empowered youth. Your partnership helps us expand our reach, develop innovative programs, and create lasting change in communities worldwide.</p>
                <div class="intro-features">
                    <div class="intro-feature">
                        <div class="intro-feature-icon">🎯</div>
                        <div class="intro-feature-text">
                            <h4>Direct Impact</h4>
                            <p>Your support directly funds programs that transform young lives</p>
                        </div>
                    </div>
                    <div class="intro-feature">
                        <div class="intro-feature-icon">🌍</div>
                        <div class="intro-feature-text">
                            <h4>Global Reach</h4>
                            <p>Connect with motivated youth across 13+ countries</p>
                        </div>
                    </div>
                    <div class="intro-feature">
                        <div class="intro-feature-icon">📊</div>
                        <div class="intro-feature-text">
                            <h4>Measurable Results</h4>
                            <p>Track your impact with detailed reports and success stories</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="intro-image">
                <video class="intro-image-main" autoplay muted loop playsinline>
                    <source src="/static/partner_video.mp4" type="video/mp4">
                </video>
                <div class="intro-image-float">
                    <div class="intro-image-float-number">700+</div>
                    <div class="intro-image-float-text">Students Taught</div>
                </div>
            </div>
        </div>
    </section>

    <section class="partner-types">
        <div class="container">
            <h2>Partnership Opportunities</h2>
            <p>Choose the partnership model that aligns with your organization's goals and values.</p>
            <div class="types-grid">
                <div class="type-card">
                    <div class="type-icon">🏢</div>
                    <h3>Corporate Partners</h3>
                    <p>Align your brand with youth empowerment. Sponsor programs, provide mentors from your team, or support initiatives through corporate giving.</p>
                    <a href="/partnership-packages" class="type-card-link">Learn More →</a>
                </div>
                <div class="type-card">
                    <div class="type-icon">🤝</div>
                    <h3>Nonprofit Partners</h3>
                    <p>Collaborate on joint programs, share resources, and amplify our collective impact. Together we can reach more young people.</p>
                    <a href="/contact" class="type-card-link">Learn More →</a>
                </div>
                <div class="type-card">
                    <div class="type-icon">🏛️</div>
                    <h3>Foundation Partners</h3>
                    <p>Support our mission through grants and funding. Help us scale programs and reach underserved communities globally.</p>
                    <a href="/partnership-packages" class="type-card-link">Learn More →</a>
                </div>
            </div>
        </div>
    </section>

    <section class="impact-section">
        <div class="container">
            <div class="impact-grid">
                <div class="impact-item">
                    <div class="impact-number">26+</div>
                    <div class="impact-label">Cities of Operation</div>
                </div>
                <div class="impact-item">
                    <div class="impact-number">12+</div>
                    <div class="impact-label">States & Provinces</div>
                </div>
                <div class="impact-item">
                    <div class="impact-number">100%</div>
                    <div class="impact-label">Volunteer-Run</div>
                </div>
                <div class="impact-item">
                    <div class="impact-number">∞</div>
                    <div class="impact-label">Potential Impact</div>
                </div>
            </div>
        </div>
    </section>

    <section class="benefits-section">
        <div class="container">
            <h2>Partnership Benefits</h2>
            <p>Join a network of organizations committed to youth empowerment and community impact.</p>
            <div class="benefits-grid">
                <div class="benefit-card">
                    <div class="benefit-icon">🎨</div>
                    <h3>Brand Visibility</h3>
                    <p>Logo placement on our website, events, and marketing materials reaching thousands of students and families.</p>
                </div>
                <div class="benefit-card">
                    <div class="benefit-icon">👥</div>
                    <h3>Talent Pipeline</h3>
                    <p>Connect with motivated, skilled young people for internships, mentorship, or future employment.</p>
                </div>
                <div class="benefit-card">
                    <div class="benefit-icon">🎤</div>
                    <h3>Speaking Opportunities</h3>
                    <p>Share your expertise at our seminars and events, positioning your organization as a thought leader.</p>
                </div>
                <div class="benefit-card">
                    <div class="benefit-icon">💼</div>
                    <h3>Employee Engagement</h3>
                    <p>Provide meaningful volunteer opportunities for your team through mentorship and workshops.</p>
                </div>
                <div class="benefit-card">
                    <div class="benefit-icon">🤝</div>
                    <h3>Co-Branded Programs</h3>
                    <p>Create custom programs that align with your CSR goals and make a tangible community impact.</p>
                </div>
                <div class="benefit-card">
                    <div class="benefit-icon">📈</div>
                    <h3>Impact Reports</h3>
                    <p>Receive detailed analytics and success stories showcasing the difference your partnership makes.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="current-partners">
        <div class="container">
            <h2>Our Partners in Action</h2>
            <p>See how our partnerships create real impact for youth around the world.</p>
            <div class="partners-grid">
                <div class="partner-card">
                    <div class="partner-card-header">
                        <h3>CICS Immigrant Youth Centre</h3>
                        <span>Community Partner</span>
                    </div>
                    <div class="partner-card-body">
                        <h4>📚 In-Person Public Speaking Classes</h4>
                        <p>We are partnering with CICS Immigrant Youth Centre to deliver in-person public speaking workshops that create space for newcomer youth to build confidence, voice, and self-expression.</p>
                        <div class="partner-video">
                            <video controls playsinline>
                                <source src="/static/partner_video.mp4" type="video/mp4">
                                Your browser does not support the video tag.
                            </video>
                        </div>
                        <span class="partner-tag">Public Speaking</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="cta-section" id="contact-form">
        <div class="container">
            <h2>Ready to <span>Make a Difference</span>?</h2>
            <p>Let's discuss how we can work together to empower youth and create lasting positive change in communities worldwide.</p>
            <div class="cta-buttons">
                <a href="/contact" class="cta-btn">Become a Partner</a>
            </div>
            <p class="contact-email">Or reach us directly at <a href="mailto:nexyouth.master@gmail.com">nexyouth.master@gmail.com</a></p>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2023 NexYouth. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

# Contact Page Template
CONTACT_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Contact NexYouth - Get in touch with us for partnerships, inquiries, and opportunities.">
    <title>Contact Us - NexYouth</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #fff;
        }

        nav {
            background: white;
            border-bottom: 1px solid #eee;
            position: sticky;
            top: 0;
            z-index: 50;
            padding: 0.8rem 2rem;
        }

        nav .container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        nav .logo {
            display: flex;
            align-items: center;
            text-decoration: none;
        }

        nav .logo img {
            height: 70px;
            width: auto;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        nav li {
            position: relative;
        }

        nav a {
            text-decoration: none;
            color: #333;
            font-size: 1rem;
            font-weight: 500;
            transition: color 0.2s;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        nav a:hover {
            color: #00d4ff;
        }

        .dropdown-menu {
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            min-width: 220px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            padding: 0.5rem 0;
            z-index: 100;
        }

        .dropdown:hover .dropdown-menu {
            display: block;
        }

        .dropdown-menu a {
            display: block;
            padding: 0.8rem 1.2rem;
            font-size: 0.9rem;
            text-transform: none;
            letter-spacing: 0;
        }

        .dropdown-menu a:hover {
            background: #f5f5f5;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .contact-hero {
            background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #0d2137 100%);
            color: white;
            text-align: center;
            padding: 6rem 2rem;
            position: relative;
            overflow: hidden;
        }

        .contact-hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 30% 20%, rgba(0, 212, 255, 0.15) 0%, transparent 50%),
                        radial-gradient(circle at 70% 80%, rgba(255, 107, 53, 0.1) 0%, transparent 50%);
            pointer-events: none;
        }

        .contact-hero .container {
            position: relative;
            z-index: 1;
        }

        .contact-hero h1 {
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            line-height: 1.2;
        }

        .contact-hero h1 span {
            background: linear-gradient(135deg, #00d4ff 0%, #00a8cc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .contact-hero p {
            font-size: 1.2rem;
            max-width: 700px;
            margin: 0 auto;
            opacity: 0.9;
        }

        .contact-content {
            padding: 6rem 2rem;
            background: white;
        }

        .contact-wrapper {
            max-width: 1200px;
            margin: 0 auto;
        }

        .contact-grid {
            display: grid;
            grid-template-columns: 1.2fr 1fr;
            gap: 4rem;
            margin-bottom: 6rem;
        }

        .contact-form h2 {
            font-size: 2.5rem;
            margin-bottom: 3rem;
            color: #1a1a2e;
            font-weight: 800;
        }

        .form-group {
            margin-bottom: 2rem;
        }

        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
            color: #333;
            font-size: 0.95rem;
        }

        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 0.85rem;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-family: inherit;
            font-size: 1rem;
            transition: border-color 0.3s, box-shadow 0.3s;
        }

        .form-group input:focus,
        .form-group textarea:focus {
            outline: none;
            border-color: #00d4ff;
            box-shadow: 0 0 0 3px rgba(0, 212, 255, 0.1);
        }

        .form-group textarea {
            resize: vertical;
            min-height: 150px;
        }

        .submit-btn {
            background: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%);
            color: white;
            padding: 1.1rem 2.5rem;
            border: none;
            border-radius: 6px;
            font-size: 1rem;
            font-weight: 700;
            cursor: pointer;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .submit-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 12px 30px rgba(0, 212, 255, 0.35);
        }

        .contact-info {
            padding-top: 2rem;
        }

        .contact-info h3 {
            font-size: 1.8rem;
            margin-bottom: 2.5rem;
            color: #1a1a2e;
            font-weight: 800;
        }

        .info-block {
            margin-bottom: 2.5rem;
            padding-bottom: 2.5rem;
            border-bottom: 1px solid #eee;
        }

        .info-block:last-child {
            border-bottom: none;
            margin-bottom: 0;
            padding-bottom: 0;
        }

        .info-block h4 {
            font-size: 1rem;
            margin-bottom: 0.8rem;
            color: #1a1a2e;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .info-block p {
            color: #555;
            font-size: 0.95rem;
            line-height: 1.8;
        }

        .info-block a {
            color: #00d4ff;
            text-decoration: none;
            font-weight: 600;
            transition: color 0.3s;
        }

        .info-block a:hover {
            color: #0099cc;
        }

        .cta-section {
            background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #0d2137 100%);
            color: white;
            padding: 5rem 2rem;
            text-align: center;
            margin-bottom: 0;
        }

        .cta-section h2 {
            font-size: 2.2rem;
            margin-bottom: 1.5rem;
            font-weight: 800;
        }

        .cta-section p {
            font-size: 1.1rem;
            max-width: 700px;
            margin: 0 auto 2.5rem;
            opacity: 0.95;
            line-height: 1.8;
        }

        .cta-btn {
            display: inline-block;
            background: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%);
            color: white;
            padding: 1rem 2.5rem;
            border-radius: 6px;
            text-decoration: none;
            font-weight: 700;
            font-size: 0.95rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .cta-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 12px 30px rgba(0, 212, 255, 0.35);
        }

        footer {
            background: #1a1a2e;
            color: white;
            padding: 4rem 2rem 2rem;
        }

        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3rem;
            margin-bottom: 3rem;
        }

        .footer-column h4 {
            font-size: 1rem;
            margin-bottom: 1.5rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #00d4ff;
            font-weight: 700;
        }

        .footer-column ul {
            list-style: none;
        }

        .footer-column li {
            margin-bottom: 0.8rem;
        }

        .footer-column a {
            color: #ddd;
            text-decoration: none;
            transition: color 0.3s;
            font-size: 0.95rem;
        }

        .footer-column a:hover {
            color: #00d4ff;
        }

        .footer-bottom {
            text-align: center;
            padding-top: 2rem;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            color: #999;
            font-size: 0.9rem;
        }

        @media (max-width: 768px) {
            .contact-hero h1 {
                font-size: 2.5rem;
            }

            .contact-grid {
                grid-template-columns: 1fr;
                gap: 2rem;
            }

            .footer-content {
                grid-template-columns: 1fr;
                gap: 2rem;
            }

            nav ul {
                gap: 1rem;
                font-size: 0.9rem;
            }
        }
    </style>
</head>
<body>
    <nav>
        <div class="container">
            <a href="/" class="logo">
                <img src="/static/logo.svg" alt="NexYouth">
            </a>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/#what-we-do">What We Do</a></li>
                <li class="dropdown">
                    <a href="/#programs">Programs ▾</a>
                    <div class="dropdown-menu">
                        <a href="/programs/skill-development">Skill Development Courses</a>
                        <a href="/programs/seminars">Expert Seminars & Talks</a>
                        <a href="/programs/mentorship">Global Mentorship Network</a>
                        <a href="/programs/environmental-competition">Environmental Youth Competition</a>
                    </div>
                </li>
                <li><a href="/#community">Community</a></li>
                <li><a href="/partner">Partner</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <section class="contact-hero">
        <div class="container">
            <h1>Get In <span>Touch</span></h1>
            <p>Have questions or want to partner with us? We'd love to hear from you. Reach out and let's create positive change together.</p>
        </div>
    </section>

    <section class="contact-content">
        <div class="contact-wrapper">
            <div class="contact-grid">
                <div class="contact-form">
                    <h2>Get In Touch</h2>
                    <form method="POST" action="https://formspree.io/f/xbdjopko" data-redirect="/success">
                        <div class="form-group">
                            <label for="name">Name</label>
                            <input type="text" id="name" name="name" required>
                        </div>
                        <div class="form-group">
                            <label for="email">Email</label>
                            <input type="email" id="email" name="email" required>
                        </div>
                        <div class="form-group">
                            <label for="subject">Subject</label>
                            <input type="text" id="subject" name="subject" required>
                        </div>
                        <div class="form-group">
                            <label for="message">Message</label>
                            <textarea id="message" name="message" required></textarea>
                        </div>
                        <button type="submit" class="submit-btn">Submit</button>
                    </form>
                </div>

                <div class="contact-info">
                    <h3>Contact Information</h3>
                    
                    <div class="info-block">
                        <h4>Visit Us</h4>
                        <p>Toronto, Canada</p>
                    </div>

                    <div class="info-block">
                        <h4>Phone</h4>
                        <p><a href="tel:+1234567890">Available upon request</a></p>
                    </div>

                    <div class="info-block">
                        <h4>Email Us</h4>
                        <p><a href="mailto:nexyouth.master@gmail.com">nexyouth.master@gmail.com</a></p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="cta-section">
        <div class="container">
            <h2>Help Us Empower Youth Globally</h2>
            <p>Your support enables us to reach more young leaders, provide quality programs, and create lasting impact in communities worldwide. Together, we can shape the future.</p>
            <a href="/#" class="cta-btn">Get Involved</a>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2023 NexYouth. All rights reserved. | Grow • Lead • Act</p>
        </div>
    </footer>
</body>
</html>
"""

@app.route('/partner')
def partner():
    return render_template('partner.html')

@app.route('/partnership-packages')
def partnership_packages():
    return render_template('partnership-packages.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/success')
def success():
    success_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Thank You - NexYouth</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }
            .success-container {
                background: white;
                border-radius: 12px;
                padding: 60px 40px;
                max-width: 500px;
                width: 100%;
                text-align: center;
                box-shadow: 0 20px 60px rgba(0, 212, 255, 0.2);
            }
            .success-icon {
                width: 80px;
                height: 80px;
                margin: 0 auto 30px;
                background: #00d4ff;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 48px;
            }
            h1 {
                color: #1a1a2e;
                font-size: 32px;
                margin-bottom: 20px;
            }
            p {
                color: #666;
                font-size: 16px;
                line-height: 1.6;
                margin-bottom: 30px;
            }
            .back-button {
                display: inline-block;
                background: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%);
                color: white;
                padding: 12px 40px;
                border-radius: 6px;
                text-decoration: none;
                font-weight: 600;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .back-button:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 25px rgba(0, 212, 255, 0.3);
            }
        </style>
    </head>
    <body>
        <div class="success-container">
            <div class="success-icon">✓</div>
            <h1>Message Received!</h1>
            <p>Thank you for reaching out to NexYouth. We've received your message and will get back to you as soon as possible. We appreciate your interest in empowering youth globally.</p>
            <a href="/" class="back-button">Return to Home</a>
        </div>
    </body>
    </html>
    """
    return success_html

@app.route('/<path:path>')
def catch_all(path):
    """Catch all routes and return the main page for client-side routing"""
    if path == 'about':
        return render_template('about.html')
    if path == 'contact':
        return render_template('contact.html')
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

# WSGI entry point for Vercel
app = app
