from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__, static_folder='public', static_url_path='/static')

@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serve static files from public folder"""
    return send_from_directory(os.path.join(os.path.dirname(__file__), 'public'), filename)

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
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2.5rem;
        }

        .program-card {
            background: white;
            border: 1px solid #eee;
            padding: 2.5rem;
            border-radius: 4px;
            transition: box-shadow 0.3s;
        }

        .program-card:hover {
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }

        .program-card h3 {
            font-size: 1.3rem;
            margin-bottom: 1rem;
            font-weight: 700;
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
            .hero h1 {
                font-size: 2rem;
            }

            .hero p {
                font-size: 1.1rem;
            }

            nav ul {
                gap: 1rem;
            }

            .action-links {
                flex-direction: column;
                gap: 1rem;
            }

            .action-links a {
                display: block;
                padding: 0.5rem;
            }

            section {
                padding: 3rem 1rem;
            }

            section h2 {
                font-size: 1.8rem;
                margin-bottom: 2rem;
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
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/#what-we-do">What We Do</a></li>
                <li class="dropdown">
                    <a href="/#programs">Programs ▾</a>
                    <div class="dropdown-menu">
                        <a href="/programs/skill-development">Skill Development Courses</a>
                        <a href="/programs/seminars">Expert Seminars & Talks</a>
                        <a href="/programs/mentorship">Global Mentorship Network</a>
                    </div>
                </li>
                <li><a href="/#community">Community</a></li>
                <li><a href="/partner">Partner</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <video autoplay muted loop playsinline>
            <source src="/static/main_background.mp4" type="video/mp4">
        </video>
        <div class="content">
            <h1>Empowering Youth to Build the Future</h1>
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
                <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform" target="_blank">Get Involved</a>
                <a href="#contact">Contact Us</a>
            </div>
        </div>
    </section>

    <!-- Programs Section -->
    <section id="programs" class="programs">
        <div class="container">
            <h2>Featured Programs</h2>
            <div class="programs-grid">
                <div class="program-card">
                    <h3>Skill Development Courses</h3>
                    <p>Comprehensive training programs designed to equip youth with in-demand skills. From digital literacy to entrepreneurship, our courses prepare students for real-world success.</p>
                </div>
                <div class="program-card">
                    <h3>Expert Seminars & Talks</h3>
                    <p>Learn directly from industry leaders and experienced professionals. Our seminars provide insights into emerging opportunities and inspire the next generation of innovators.</p>
                </div>
                <div class="program-card">
                    <h3>Global Mentorship Network</h3>
                    <p>Get paired with mentors who can guide your personal and professional development. Our mentors bring real-world experience and genuine commitment to your growth.</p>
                </div>
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
                    <div class="testimonial-author">Sarah Johnson</div>
                    <div class="testimonial-title">Course Participant</div>
                </div>
                <div class="testimonial-card">
                    <div class="testimonial-quote">"Being part of this community showed me that I'm not alone in my journey. The support and guidance from mentors made all the difference in my success."</div>
                    <div class="testimonial-author">Marcus Chen</div>
                    <div class="testimonial-title">Program Graduate</div>
                </div>
                <div class="testimonial-card">
                    <div class="testimonial-quote">"The practical skills and confidence I gained through NexYouth's programs have been instrumental in landing my dream internship and building my career."</div>
                    <div class="testimonial-author">Amina Patel</div>
                    <div class="testimonial-title">Scholarship Winner</div>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section id="contact" class="cta-section">
        <div class="container">
            <h2>Join Our Community Today</h2>
            <p style="font-size: 1.1rem; margin-bottom: 2rem;">Ready to start your journey? Connect with us on our platforms or fill out our form to get involved.</p>
            <div class="action-links" style="justify-content: center;">
                <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform" target="_blank" style="color: #ff6b35;">Get Involved</a>
                <a href="https://discord.com/invite/qqT2ce3NY7" target="_blank" style="color: #ff6b35;">Discord</a>
                <a href="https://www.instagram.com/nexyouth.ngo/" target="_blank" style="color: #ff6b35;">Instagram</a>
                <a href="https://www.linkedin.com/company/nexyouth-society/" target="_blank" style="color: #ff6b35;">LinkedIn</a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer id="contact-footer">
        <div class="container">
            <div class="links">
                <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform" target="_blank">Get Involved</a>
                <a href="https://discord.com/invite/qqT2ce3NY7" target="_blank">Discord</a>
                <a href="https://www.instagram.com/nexyouth.ngo/" target="_blank">Instagram</a>
                <a href="https://www.linkedin.com/company/nexyouth-society/" target="_blank">LinkedIn</a>
            </div>
            <p>&copy; 2023 NexYouth. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

# ============== ABOUT PAGE ==============
ABOUT_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="NexYouth - Meet our team of passionate volunteers.">
    <title>About - NexYouth</title>
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
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            min-width: 220px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
            border-radius: 8px;
            opacity: 0;
            visibility: hidden;
            transform: translateY(10px);
            transition: all 0.3s ease;
            padding: 0.5rem 0;
            z-index: 100;
        }

        .dropdown-menu li {
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

        .dropdown:hover .dropdown-menu {
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        /* About Hero */
        .about-hero {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: white;
            text-align: center;
            padding: 6rem 2rem;
        }

        .about-hero h1 {
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
        }

        .about-hero p {
            font-size: 1.2rem;
            max-width: 800px;
            margin: 0 auto;
            opacity: 0.9;
            line-height: 1.8;
        }

        /* Team Section */
        .team-section {
            padding: 5rem 2rem;
            background: #f9f9f9;
        }

        .team-section h2 {
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 3rem;
            text-align: center;
        }

        .team-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .team-card {
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .team-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
        }

        .team-card img {
            width: 100%;
            height: 280px;
            object-fit: cover;
        }

        .team-card-content {
            padding: 1.5rem;
        }

        .team-role {
            color: #ff6b35;
            font-size: 0.85rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 0.5rem;
        }

        .team-card h3 {
            font-size: 1.3rem;
            font-weight: 700;
            margin-bottom: 0.8rem;
            color: #1a1a2e;
        }

        .team-card p {
            color: #666;
            font-size: 0.95rem;
            line-height: 1.7;
        }

        /* Join CTA */
        .join-cta {
            background: #ff6b35;
            color: white;
            text-align: center;
            padding: 5rem 2rem;
        }

        .join-cta h2 {
            font-size: 2rem;
            margin-bottom: 1.5rem;
            color: white;
        }

        .join-cta p {
            font-size: 1.1rem;
            margin-bottom: 2rem;
            opacity: 0.95;
        }

        .join-btn {
            display: inline-block;
            background: white;
            color: #ff6b35;
            padding: 1rem 2.5rem;
            border-radius: 4px;
            text-decoration: none;
            font-weight: 600;
            font-size: 1rem;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .join-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
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
            .about-hero h1 {
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

            .team-grid {
                grid-template-columns: 1fr;
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
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/#what-we-do">What We Do</a></li>
                <li class="dropdown">
                    <a href="/#programs">Programs</a>
                    <ul class="dropdown-menu">
                        <li><a href="/programs/skill-development">Skill Development Courses</a></li>
                        <li><a href="/programs/seminars">Expert Seminars & Talks</a></li>
                        <li><a href="/programs/mentorship">Global Mentorship Network</a></li>
                    </ul>
                </li>
                <li><a href="/#community">Community</a></li>
                <li><a href="/partner">Partner</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- About Hero -->
    <section class="about-hero">
        <div class="container">
            <h1>The Team Behind NexYouth.</h1>
            <p>At the heart of NexYouth is our inspiring community of volunteers — passionate individuals who dedicate their time, skills, and creativity to driving meaningful change. Coming from diverse backgrounds in science, education, advocacy, and the arts, our volunteers share a common commitment to protecting the environment and empowering youth.</p>
        </div>
    </section>

    <!-- Team Section -->
    <section class="team-section">
        <div class="container">
            <h2>Meet the Team</h2>
            <div class="team-grid">
                <!-- Justin Huang -->
                <div class="team-card">
                    <img src="https://www.nexyouth.org/Member_Jhuan1.jpg" alt="Justin Huang">
                    <div class="team-card-content">
                        <div class="team-role">Co Founder</div>
                        <h3>Justin Huang</h3>
                        <p>Justin is the co-founder of NexYouth. He is interested in how young people learn through experience, connection, and initiative, and focuses on creating spaces where youth can explore ideas and take ownership of what they care about.</p>
                    </div>
                </div>

                <!-- Max Wen -->
                <div class="team-card">
                    <img src="https://www.nexyouth.org/Member_Mwen1.jpg" alt="Max Wen">
                    <div class="team-card-content">
                        <div class="team-role">Co Founder</div>
                        <h3>Max Wen</h3>
                        <p>Hi, I'm Max, one of the co-founders of NexYouth. I'm in Grade 9 and have been debating and teaching for over 2 years! I enjoy public speaking, STEM, and content creation(@MaxW3n).</p>
                    </div>
                </div>

                <!-- Stephanie Uzea -->
                <div class="team-card">
                    <img src="https://www.nexyouth.org/Member_Suzea1.png" alt="Stephanie Uzea">
                    <div class="team-card-content">
                        <div class="team-role">Canada President & Director of Operations</div>
                        <h3>Stephanie Uzea</h3>
                        <p>Stephanie is an aspiring environmental engineer with a passion for writing. She's written multiple comics about her brother if he were a superhero as well as a science fiction trilogy. In her free time, she likes trying out new foods and cross-country running.</p>
                    </div>
                </div>

                <!-- Xuhan Yang -->
                <div class="team-card">
                    <img src="https://www.nexyouth.org/Member_Xyang1.jpg" alt="Xuhan Yang">
                    <div class="team-card-content">
                        <div class="team-role">Director of Technology</div>
                        <h3>Xuhan Yang</h3>
                        <p>Hi I'm Xuhan! I'm a high schooler passionate about programming, math, or anything STEM related!</p>
                    </div>
                </div>

                <!-- Ethan Luo -->
                <div class="team-card">
                    <img src="https://www.nexyouth.org/Member_Eluo1.png" alt="Ethan Luo">
                    <div class="team-card-content">
                        <div class="team-role">Oakville Chapter President</div>
                        <h3>Ethan Luo</h3>
                        <p>Ethan is a Grade 10 student at Abbey Park High School in Oakville. With 2 years of competitive debate experience, he has advanced at prestigious tournaments such as Harvard WSDC, Queens BPHS, McGill BPHS, and Hart House High Schools. Outside debate, he enjoys clarinet, trail running, and co-hosting Perception Podcast.</p>
                    </div>
                </div>

                <!-- Chloe Huang -->
                <div class="team-card">
                    <img src="https://www.nexyouth.org/Member_Chuan1.jpg" alt="Chloe Huang">
                    <div class="team-card-content">
                        <div class="team-role">Secretary</div>
                        <h3>Chloe Huang</h3>
                        <p>Chloe is a Grade 11 student at Earl of March High School. She is an avid volleyball player and loves sports!</p>
                    </div>
                </div>

                <!-- Rachel Wei -->
                <div class="team-card">
                    <img src="https://www.nexyouth.org/Member_Rwei1.png" alt="Rachel Wei">
                    <div class="team-card-content">
                        <div class="team-role">Coquitlam Chapter President</div>
                        <h3>Rachel Wei</h3>
                        <p>Rachel Wei is a rising senior at Port Moody Secondary School. She loves playing basketball, is an avid debater, and loves her pet cat! She is also a passionate environmentalist.</p>
                    </div>
                </div>

                <!-- Keerti Joshi -->
                <div class="team-card">
                    <img src="https://www.nexyouth.org/Member_Kjosh1.png" alt="Keerti Joshi">
                    <div class="team-card-content">
                        <div class="team-role">Debate Coach</div>
                        <h3>Keerti Joshi</h3>
                        <p>I'm Keerti, I'm a grade 11 student at Upper Canada College. I've been debating since Grade 8 and I debate in both WSDC and BP formats. I am a new member of the Canadian National Debating Team and have competed and won in many tournaments run by Canadian Universities.</p>
                    </div>
                </div>

                <!-- Kristen Yip -->
                <div class="team-card">
                    <img src="https://www.nexyouth.org/Member_Kyip1.png" alt="Kristen Yip">
                    <div class="team-card-content">
                        <div class="team-role">Debate Coach</div>
                        <h3>Kristen Yip</h3>
                        <p>Kristen Y (she/her) is a grade 9 student and avid debater. Achievements include: Top 4th speaker+top jr speaker (Harthouse Winter Open), top 3rd speaker + grand finalist (Harthouse Summer Open), grand finalist + 4th jr speaker (Autumnloo 2024).</p>
                    </div>
                </div>

                <!-- Cody Zhang -->
                <div class="team-card">
                    <img src="https://www.nexyouth.org/Member_Czhan1.png" alt="Cody Zhang">
                    <div class="team-card-content">
                        <div class="team-role">Economics Instructor</div>
                        <h3>Cody Zhang</h3>
                        <p>Cody Zhang is a high schooler from Toronto and scored a 5 on AP Micro and makes economics simple, fun, and engaging!</p>
                    </div>
                </div>

                <!-- Jeffrey Liu -->
                <div class="team-card">
                    <img src="https://www.nexyouth.org/Member_Jliu1.png" alt="Jeffrey Liu">
                    <div class="team-card-content">
                        <div class="team-role">Debate Coach</div>
                        <h3>Jeffrey Liu</h3>
                        <p>Hi, I'm Jeffrey! I am a grade 11 student at Milliken Mills High School. In my free time I love cooking food, listening to music (especially hip hop and r&b), and working out! I am ecstatic to work with NexYouth this year to continue to promote accessibility in debate and further youth engagement!</p>
                    </div>
                </div>

                <!-- Amy Liu -->
                <div class="team-card">
                    <img src="https://www.nexyouth.org/Member_Aliu1.png" alt="Amy Liu">
                    <div class="team-card-content">
                        <div class="team-role">Debate Coach</div>
                        <h3>Amy Liu</h3>
                        <p>Amy is a G10 student and a competitive debater who has won many debate tournaments.</p>
                    </div>
                </div>

                <!-- Ferrari Zhang -->
                <div class="team-card">
                    <img src="https://www.nexyouth.org/Member_Fzhan1.jpg" alt="Ferrari Zhang">
                    <div class="team-card-content">
                        <div class="team-role">Debate Coach</div>
                        <h3>Ferrari Zhang</h3>
                        <p>Ferrari is a G10 student and a competitive debater, who loves argumentation and refutation!</p>
                    </div>
                </div>

                <!-- Terrence Guo -->
                <div class="team-card">
                    <img src="https://www.nexyouth.org/Member_Tguo1.png" alt="Terrence Guo">
                    <div class="team-card-content">
                        <div class="team-role">Debate Coach</div>
                        <h3>Terrence Guo</h3>
                        <p>Terrence is a G12 student and a competitive debater at the national level, winning many debating tournaments, including being the top speaker at Hart House High Schools.</p>
                    </div>
                </div>

                <!-- Yunfei Shuai -->
                <div class="team-card">
                    <img src="https://www.nexyouth.org/Member_Yshua1.png" alt="Yunfei Shuai">
                    <div class="team-card-content">
                        <div class="team-role">Contests Organizer</div>
                        <h3>Yunfei Shuai</h3>
                        <p>Yunfei wrote her first story when she was 7 years old and never looked back since. She is an avid sci-fi enthusiast and an aspiring astrophysicist. Most of the time she can be found bingeing figure skating competitions and Arcane.</p>
                    </div>
                </div>

                <!-- Susan Zheng -->
                <div class="team-card">
                    <img src="https://www.nexyouth.org/Member_Szhen1.png" alt="Susan Zheng">
                    <div class="team-card-content">
                        <div class="team-role">Contests Organizer</div>
                        <h3>Susan Zheng</h3>
                        <p>Susan finds way too much enjoyment in daydreaming about fictional scenarios and promising herself she'll finish a project tomorrow. A sci-fi fanatic, she obsesses over very specific mathematical and scientific concepts she knows she will never understand.</p>
                    </div>
                </div>

                <!-- Shahrad Islam -->
                <div class="team-card">
                    <img src="https://www.nexyouth.org/Member_Sisla1.png" alt="Shahrad Islam">
                    <div class="team-card-content">
                        <div class="team-role">Science Instructor</div>
                        <h3>Shahrad Islam</h3>
                        <p>Hi! My name is Shahrad! Some things you should know about me are that I like playing sports, playing instruments, watching movies and shows, and I really like cats! I am happy to be a part of the NexYouth Team helping mentor and tutor others!</p>
                    </div>
                </div>

                <!-- Ronnie Liu -->
                <div class="team-card">
                    <img src="https://www.nexyouth.org/Member_Rliu1.png" alt="Ronnie Liu">
                    <div class="team-card-content">
                        <div class="team-role">Science Instructor</div>
                        <h3>Ronnie Liu</h3>
                        <p>Hello, my name is Ronnie Liu. I am a gifted grade 10 scholar at Richmond Hill High School. I love teaching because I enjoy watching children learn and discover new things, as well as meet new friends along the way.</p>
                    </div>
                </div>

                <!-- Rest of Team -->
                <div class="team-card">
                    <img src="https://media.istockphoto.com/id/1472932742/photo/group-of-multigenerational-people-hugging-each-others-support-multiracial-and-diversity.jpg?s=612x612&w=0&k=20&c=Zm1MthU_G_LzfjBFBaMORRnuBhMsCjPQ38Ksfg4zl9g=" alt="Rest of the Team">
                    <div class="team-card-content">
                        <div class="team-role">Instructors & Volunteers</div>
                        <h3>Rest of the Team</h3>
                        <p>More to come! We have a large team of dedicated instructors and volunteers who help make our programs possible.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Join CTA -->
    <section class="join-cta">
        <div class="container">
            <h2>Join Our Community</h2>
            <p>Ready to make a difference? Become part of our passionate team of changemakers.</p>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform" target="_blank" class="join-btn">Get Involved</a>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="links">
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform" target="_blank">Get Involved</a>
                <a href="https://discord.com/invite/qqT2ce3NY7" target="_blank">Discord</a>
                <a href="https://www.instagram.com/nexyouth.ngo/" target="_blank">Instagram</a>
                <a href="https://www.linkedin.com/company/nexyouth-society/" target="_blank">LinkedIn</a>
            </div>
            <p>&copy; 2023 NexYouth. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

@app.route('/about')
def about():
    return render_template_string(ABOUT_TEMPLATE)

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

        .dropdown-menu {
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            min-width: 220px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
            border-radius: 8px;
            opacity: 0;
            visibility: hidden;
            transform: translateY(10px);
            transition: all 0.3s ease;
            padding: 0.5rem 0;
            z-index: 100;
        }

        .dropdown-menu li {
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

        .dropdown:hover .dropdown-menu {
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
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
                    <a href="/#programs">Programs</a>
                    <ul class="dropdown-menu">
                        <li><a href="/programs/skill-development">Skill Development Courses</a></li>
                        <li><a href="/programs/seminars">Expert Seminars & Talks</a></li>
                        <li><a href="/programs/mentorship">Global Mentorship Network</a></li>
                    </ul>
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
            <p>Empowering youth with practical skills for the future. Our comprehensive courses cover essential topics from public speaking to environmental science, designed to help you grow and lead.</p>
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
                    <p>Introduction to science, technology, engineering, and mathematics concepts through engaging experiments and projects.</p>
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
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform" target="_blank" class="cta-btn">Enroll Now</a>
        </div>
    </section>

    <footer>
        <div class="container">
            <div class="links">
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform" target="_blank">Get Involved</a>
                <a href="https://discord.com/invite/qqT2ce3NY7" target="_blank">Discord</a>
                <a href="https://www.instagram.com/nexyouth.ngo/" target="_blank">Instagram</a>
                <a href="https://www.linkedin.com/company/nexyouth-society/" target="_blank">LinkedIn</a>
            </div>
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

        .dropdown-menu {
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            min-width: 220px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
            border-radius: 8px;
            opacity: 0;
            visibility: hidden;
            transform: translateY(10px);
            transition: all 0.3s ease;
            padding: 0.5rem 0;
            z-index: 100;
        }

        .dropdown-menu li {
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

        .dropdown:hover .dropdown-menu {
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
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
                    <a href="/#programs">Programs</a>
                    <ul class="dropdown-menu">
                        <li><a href="/programs/skill-development">Skill Development Courses</a></li>
                        <li><a href="/programs/seminars">Expert Seminars & Talks</a></li>
                        <li><a href="/programs/mentorship">Global Mentorship Network</a></li>
                    </ul>
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
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform" target="_blank" class="cta-btn">Sign Up</a>
        </div>
    </section>

    <footer>
        <div class="container">
            <div class="links">
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform" target="_blank">Get Involved</a>
                <a href="https://discord.com/invite/qqT2ce3NY7" target="_blank">Discord</a>
                <a href="https://www.instagram.com/nexyouth.ngo/" target="_blank">Instagram</a>
                <a href="https://www.linkedin.com/company/nexyouth-society/" target="_blank">LinkedIn</a>
            </div>
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

        .dropdown-menu {
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            min-width: 220px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
            border-radius: 8px;
            opacity: 0;
            visibility: hidden;
            transform: translateY(10px);
            transition: all 0.3s ease;
            padding: 0.5rem 0;
            z-index: 100;
        }

        .dropdown-menu li {
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

        .dropdown:hover .dropdown-menu {
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
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
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
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
                    <a href="/#programs">Programs</a>
                    <ul class="dropdown-menu">
                        <li><a href="/programs/skill-development">Skill Development Courses</a></li>
                        <li><a href="/programs/seminars">Expert Seminars & Talks</a></li>
                        <li><a href="/programs/mentorship">Global Mentorship Network</a></li>
                    </ul>
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
                <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform" target="_blank" class="cta-btn">Find a Mentor</a>
                <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform" target="_blank" class="cta-btn secondary">Become a Mentor</a>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <div class="links">
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform" target="_blank">Get Involved</a>
                <a href="https://discord.com/invite/qqT2ce3NY7" target="_blank">Discord</a>
                <a href="https://www.instagram.com/nexyouth.ngo/" target="_blank">Instagram</a>
                <a href="https://www.linkedin.com/company/nexyouth-society/" target="_blank">LinkedIn</a>
            </div>
            <p>&copy; 2023 NexYouth. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

# Program Routes
@app.route('/programs/skill-development')
def skill_development():
    return render_template_string(SKILL_DEVELOPMENT_TEMPLATE)

@app.route('/programs/seminars')
def seminars():
    return render_template_string(SEMINARS_TEMPLATE)

@app.route('/programs/mentorship')
def mentorship():
    return render_template_string(MENTORSHIP_TEMPLATE)

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

        .dropdown-menu {
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            min-width: 220px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
            border-radius: 8px;
            opacity: 0;
            visibility: hidden;
            transform: translateY(10px);
            transition: all 0.3s ease;
            padding: 0.5rem 0;
            z-index: 100;
        }

        .dropdown-menu li {
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

        .dropdown:hover .dropdown-menu {
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
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
                    <a href="/#programs">Programs</a>
                    <ul class="dropdown-menu">
                        <li><a href="/programs/skill-development">Skill Development Courses</a></li>
                        <li><a href="/programs/seminars">Expert Seminars & Talks</a></li>
                        <li><a href="/programs/mentorship">Global Mentorship Network</a></li>
                    </ul>
                </li>
                <li><a href="/#community">Community</a></li>
                <li><a href="/partner">Partner</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/#contact">Contact</a></li>
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
                    <a href="#contact-form" class="type-card-link">Learn More →</a>
                </div>
                <div class="type-card">
                    <div class="type-icon">🤝</div>
                    <h3>Nonprofit Partners</h3>
                    <p>Collaborate on joint programs, share resources, and amplify our collective impact. Together we can reach more young people.</p>
                    <a href="#contact-form" class="type-card-link">Learn More →</a>
                </div>
                <div class="type-card">
                    <div class="type-icon">🏛️</div>
                    <h3>Foundation Partners</h3>
                    <p>Support our mission through grants and funding. Help us scale programs and reach underserved communities globally.</p>
                    <a href="#contact-form" class="type-card-link">Learn More →</a>
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
                        <p>We partnered with CICS Immigrant Youth Centre to deliver in-person public speaking workshops that create space for newcomer youth to build confidence, voice, and self-expression.</p>
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
                <a href="mailto:nexyouth.master@gmail.com?subject=Partnership Interest" class="cta-btn">Become a Partner</a>
                <a href="mailto:nexyouth.master@gmail.com" class="cta-btn secondary">Schedule a Call</a>
            </div>
            <p class="contact-email">Or reach us directly at <a href="mailto:nexyouth.master@gmail.com">nexyouth.master@gmail.com</a></p>
        </div>
    </section>

    <footer>
        <div class="container">
            <div class="links">
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="/partner">Partner</a>
                <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform" target="_blank">Get Involved</a>
                <a href="https://discord.com/invite/qqT2ce3NY7" target="_blank">Discord</a>
                <a href="https://www.instagram.com/nexyouth.ngo/" target="_blank">Instagram</a>
                <a href="https://www.linkedin.com/company/nexyouth-society/" target="_blank">LinkedIn</a>
            </div>
            <p>&copy; 2023 NexYouth. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

@app.route('/partner')
def partner():
    return render_template_string(PARTNER_TEMPLATE)

@app.route('/<path:path>')
def catch_all(path):
    """Catch all routes and return the main page for client-side routing"""
    if path == 'about':
        return render_template_string(ABOUT_TEMPLATE)
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

# WSGI entry point for Vercel
app = app
