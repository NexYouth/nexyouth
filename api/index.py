from flask import Flask, render_template_string, send_from_directory
import os
import re

app = Flask(__name__, static_folder='../public', static_url_path='/static')

@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serve static files from public folder"""
    try:
        return send_from_directory(os.path.join(os.path.dirname(__file__), '../public'), filename)
    except:
        return "", 404

# Unified Navigation and Styling
NAVIGATION_HTML = """
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
"""

NAVIGATION_STYLES = """
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

        @media (max-width: 768px) {
            nav ul {
                gap: 1rem;
                flex-wrap: wrap;
                justify-content: center;
            }
            nav .container {
                flex-direction: column;
                gap: 1rem;
            }
            nav .logo img {
                height: 50px;
            }
        }
"""

def update_navigation_and_logo(html_content):
    """Update navigation and logo in HTML content"""
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', NAVIGATION_HTML, html_content, flags=re.DOTALL)
    html_content = re.sub(r'<img[^>]*?src="[^"]*nexyouthlogo[^"]*?"', '<img src="/static/logo.svg" alt="NexYouth"', html_content)
    html_content = re.sub(r'<img[^>]*?alt="NexYouth"[^>]*?src="[^"]*"', '<img src="/static/logo.svg" alt="NexYouth"', html_content)
    if '<style>' not in html_content and NAVIGATION_STYLES not in html_content:
        style_injection = f"<style>\n{NAVIGATION_STYLES}\n"
        html_content = re.sub(r'<style>', style_injection, html_content, count=1)
    return html_content

HOME_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NexYouth - Empower Youth. Shape the Future.</title>
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

        """ + NAVIGATION_STYLES + """

        .hero {
            background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #0d2137 100%);
            color: white;
            text-align: center;
            padding: 8rem 2rem;
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
            background: radial-gradient(circle at 30% 20%, rgba(0, 212, 255, 0.15) 0%, transparent 50%),
                        radial-gradient(circle at 70% 80%, rgba(255, 107, 53, 0.1) 0%, transparent 50%);
            pointer-events: none;
        }

        .hero .container {
            position: relative;
            z-index: 1;
            max-width: 1200px;
            margin: 0 auto;
        }

        .hero h1 {
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            line-height: 1.2;
        }

        .hero h1 span {
            background: linear-gradient(135deg, #00d4ff 0%, #00a8cc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .hero p {
            font-size: 1.3rem;
            max-width: 700px;
            margin: 0 auto 2.5rem;
            opacity: 0.9;
            line-height: 1.8;
        }

        .hero-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
        }

        .btn {
            display: inline-block;
            padding: 1rem 2.5rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            font-size: 1.1rem;
            transition: all 0.3s ease;
        }

        .btn-primary {
            background: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%);
            color: white;
            box-shadow: 0 5px 20px rgba(0, 212, 255, 0.3);
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(0, 212, 255, 0.4);
        }

        .btn-secondary {
            background: transparent;
            color: white;
            border: 2px solid rgba(255, 255, 255, 0.3);
        }

        .btn-secondary:hover {
            background: rgba(255, 255, 255, 0.1);
            border-color: rgba(255, 255, 255, 0.5);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .stats {
            display: flex;
            justify-content: center;
            gap: 4rem;
            margin-top: 3rem;
            flex-wrap: wrap;
        }

        .stat {
            text-align: center;
        }

        .stat-number {
            font-size: 2.5rem;
            font-weight: 800;
            color: #00d4ff;
        }

        .stat-label {
            font-size: 0.95rem;
            opacity: 0.8;
            margin-top: 0.3rem;
        }

        .mission-section {
            padding: 6rem 2rem;
            background: white;
        }

        .mission-content {
            max-width: 800px;
            margin: 0 auto;
            text-align: center;
        }

        .mission-content h2 {
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
            color: #1a1a2e;
        }

        .mission-content p {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #555;
        }

        .programs-section {
            padding: 6rem 2rem;
            background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);
        }

        .programs-section h2 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            text-align: center;
            color: #1a1a2e;
        }

        .programs-section > p {
            text-align: center;
            color: #666;
            margin-bottom: 3rem;
        }

        .programs-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            max-width: 1100px;
            margin: 0 auto;
        }

        .program-card {
            background: white;
            border-radius: 20px;
            padding: 2.5rem;
            text-align: center;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
            transition: all 0.4s ease;
        }

        .program-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 60px rgba(0, 212, 255, 0.15);
        }

        .program-icon {
            font-size: 3rem;
            margin-bottom: 1.5rem;
        }

        .program-card h3 {
            font-size: 1.4rem;
            margin-bottom: 1rem;
            color: #1a1a2e;
        }

        .program-card p {
            font-size: 1rem;
            color: #666;
            line-height: 1.7;
            margin-bottom: 1.5rem;
        }

        .program-link {
            color: #00d4ff;
            font-weight: 600;
            text-decoration: none;
            transition: gap 0.3s ease;
        }

        .program-link:hover {
            text-decoration: underline;
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
            .hero h1 {
                font-size: 2.2rem;
            }
            .stats {
                gap: 2rem;
            }
        }
    </style>
</head>
<body>
    """ + NAVIGATION_HTML + """

    <section class="hero">
        <div class="container">
            <h1>Creating Space for Youth. <span>Shape the Future.</span></h1>
            <p>NexYouth provides global youth with skill development, mentorship, and hands-on opportunities to become changemakers in their communities.</p>
            <div class="hero-buttons">
                <a href="#programs" class="btn btn-primary">Learn More</a>
                <a href="/partner" class="btn btn-secondary">Become a Partner</a>
            </div>
            <div class="stats">
                <div class="stat">
                    <div class="stat-number">5000+</div>
                    <div class="stat-label">Youth Impacted</div>
                </div>
                <div class="stat">
                    <div class="stat-number">13+</div>
                    <div class="stat-label">Countries</div>
                </div>
                <div class="stat">
                    <div class="stat-number">90+</div>
                    <div class="stat-label">Schools</div>
                </div>
            </div>
        </div>
    </section>

    <section class="mission-section" id="what-we-do">
        <div class="mission-content">
            <h2>Our Mission</h2>
            <p>Empowering youth through skill development, global mentorship networks, and hands-on project opportunities to create meaningful impact.</p>
            <p>At NexYouth, we're committed to empowering youth through skill development, global mentorship networks, and hands-on project opportunities. We believe every young person has the potential to become a changemaker in their community and beyond.</p>
        </div>
    </section>

    <section class="programs-section" id="programs">
        <div class="container">
            <h2>Our Programs</h2>
            <p>Comprehensive learning experiences designed to develop skills and inspire action</p>
            <div class="programs-grid">
                <div class="program-card">
                    <div class="program-icon">📚</div>
                    <h3>Skill Development Courses</h3>
                    <p>From public speaking to STEM, our comprehensive courses equip youth with in-demand skills for real-world success.</p>
                    <a href="/programs/skill-development" class="program-link">Explore →</a>
                </div>
                <div class="program-card">
                    <div class="program-icon">🎤</div>
                    <h3>Expert Seminars</h3>
                    <p>Learn directly from industry leaders and professionals. Our seminars provide insights into emerging opportunities.</p>
                    <a href="/programs/seminars" class="program-link">Explore →</a>
                </div>
                <div class="program-card">
                    <div class="program-icon">🤝</div>
                    <h3>Mentorship Network</h3>
                    <p>Connect with experienced mentors globally. Get personalized guidance to navigate challenges and achieve your goals.</p>
                    <a href="/programs/mentorship" class="program-link">Explore →</a>
                </div>
            </div>
        </div>
    </section>

    <section id="community" style="padding: 6rem 2rem; background: white;">
        <div class="container" style="text-align: center;">
            <h2 style="font-size: 2.5rem; margin-bottom: 3rem; color: #1a1a2e;">Join Our Community</h2>
            <p style="font-size: 1.1rem; color: #666; margin-bottom: 2rem;">Become part of a global movement of empowered youth changemakers.</p>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform" class="btn btn-primary">Get Involved</a>
        </div>
    </section>

    <footer id="contact">
        <div class="container">
            <p>&copy; 2025 NexYouth. All rights reserved. | Grow • Lead • Act</p>
        </div>
    </footer>
</body>
</html>
"""

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

        """ + NAVIGATION_STYLES + """

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

        footer p {
            color: #999;
            font-size: 0.9rem;
        }

        @media (max-width: 1024px) {
            .intro-grid {
                grid-template-columns: 1fr;
                gap: 3rem;
            }
        }

        @media (max-width: 768px) {
            .partner-hero h1 {
                font-size: 2.2rem;
            }
            .hero-stats {
                gap: 2rem;
            }
        }
    </style>
</head>
<body>
    """ + NAVIGATION_HTML + """

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

    <section class="cta-section">
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
            <p>&copy; 2025 NexYouth. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

ABOUT_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us - NexYouth</title>
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

        """ + NAVIGATION_STYLES + """

        .hero {
            background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #0d2137 100%);
            color: white;
            text-align: center;
            padding: 8rem 2rem;
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
            background: radial-gradient(circle at 30% 20%, rgba(0, 212, 255, 0.15) 0%, transparent 50%),
                        radial-gradient(circle at 70% 80%, rgba(255, 107, 53, 0.1) 0%, transparent 50%);
            pointer-events: none;
        }

        .hero .container {
            position: relative;
            z-index: 1;
        }

        .hero h1 {
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            line-height: 1.2;
        }

        .hero p {
            font-size: 1.2rem;
            max-width: 700px;
            margin: 0 auto 0;
            opacity: 0.9;
            line-height: 1.8;
        }

        .mission-section {
            padding: 6rem 2rem;
            background: white;
        }

        .mission-content {
            max-width: 800px;
            margin: 0 auto;
            text-align: center;
        }

        .mission-content h2 {
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
            color: #1a1a2e;
        }

        .mission-content p {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #555;
        }

        .team-section {
            background: white;
            padding: 6rem 2rem;
        }

        .team-section h2 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            text-align: center;
            color: #1a1a2e;
        }

        .team-section > p {
            text-align: center;
            color: #666;
            margin-bottom: 3rem;
        }

        .team-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2.5rem;
            max-width: 1200px;
            margin: 3rem auto;
        }

        .team-member {
            text-align: center;
            background: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
            transition: all 0.3s ease;
        }

        .team-member:hover {
            box-shadow: 0 8px 24px rgba(0, 212, 255, 0.1);
            transform: translateY(-2px);
        }

        .team-member-image {
            width: 160px;
            height: 160px;
            border-radius: 50%;
            margin: 0 auto 1.2rem;
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
            font-size: 1.05rem;
            color: #1a1a2e;
            margin-bottom: 0.75rem;
            font-weight: 700;
            line-height: 1.4;
        }

        .team-member .role {
            font-size: 0.85rem;
            color: #00d4ff;
            font-weight: 600;
            margin-bottom: 1rem;
            display: block;
        }

        .team-member .bio {
            font-size: 0.9rem;
            line-height: 1.65;
            color: #666;
            text-align: center;
            margin: 0;
        }

        @media (max-width: 1200px) {
            .team-grid {
                grid-template-columns: repeat(3, 1fr);
            }
        }

        @media (max-width: 768px) {
            .team-grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 2rem;
            }
        }

        @media (max-width: 480px) {
            .team-grid {
                grid-template-columns: 1fr;
            }
        }

        .community-section {
            background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #0d2137 100%);
            color: white;
            text-align: center;
            padding: 5rem 2rem;
            position: relative;
        }

        .community-section h2 {
            color: white;
            margin-bottom: 1.5rem;
        }

        .community-section p {
            color: rgba(255, 255, 255, 0.9);
            max-width: 800px;
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
            font-size: 1.1rem;
            margin-top: 2rem;
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
            .hero h1 {
                font-size: 2.2rem;
            }
            .mission-content h2 {
                font-size: 1.8rem;
            }
        }
    </style>
</head>
<body>
    """ + NAVIGATION_HTML + """

    <section class="hero">
        <div class="container">
            <h1>About NexYouth</h1>
            <p>Empowering youth through skill development, mentorship, and hands-on opportunities to create meaningful change.</p>
        </div>
    </section>

    <section class="mission-section">
        <div class="mission-content">
            <h2>Our Mission</h2>
            <p>At the heart of NexYouth is our inspiring community of volunteers — passionate individuals who dedicate their time, skills, and creativity to driving meaningful change.</p>
            <p>Coming from diverse backgrounds in science, education, advocacy, and the arts, our volunteers share a common commitment to protecting the environment and empowering youth.</p>
        </div>
    </section>

    <section class="mission-section">
        <div class="mission-content">
            <h2>Our Story</h2>
            <p>NexYouth was founded by passionate high school students who believe in the power of youth to create meaningful change. Together, they've built a platform that connects young people with opportunities for growth and impact.</p>
        </div>
    </section>

    <section class="team-section">
        <div class="mission-content">
            <h2>Our Team</h2>
            <p>Meet the passionate youth leaders who make NexYouth possible.</p>
            <div class="team-grid" style="margin-top: 3rem;">
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Jhuan1.jpg" alt="Justin Huang" onerror="this.style.display='none'">
                    </div>
                    <h3>Justin Huang</h3>
                    <span class="role">Co-Founder</span>
                    <p class="bio">Justin is the co-founder of NexYouth. He is interested in how young people learn through experience, connection, and initiative, and focuses on creating spaces where youth can explore ideas and take ownership of what they care about.</p>
                </div>
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Mwen1.jpg" alt="Max Wen" onerror="this.style.display='none'">
                    </div>
                    <h3>Max Wen</h3>
                    <span class="role">Co-Founder</span>
                    <p class="bio">Hi, I'm Max, one of the co-founders of NexYouth. I'm in Grade 9 and have been debating and teaching for over 2 years! I enjoy public speaking, STEM, and content creation.</p>
                </div>
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Suzea1.png" alt="Stephanie Uzea" onerror="this.style.display='none'">
                    </div>
                    <h3>Stephanie Uzea</h3>
                    <span class="role">Canada Head & Director of Operations</span>
                    <p class="bio">Stephanie is an aspiring environmental engineer with a passion for writing. She's written multiple comics about her brother if he were a superhero as well as a science fiction trilogy. In her free time, she likes trying out new foods and cross-country running.</p>
                </div>
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Eluo1.png" alt="Ethan Luo" onerror="this.style.display='none'">
                    </div>
                    <h3>Ethan Luo</h3>
                    <span class="role">Debate Coach</span>
                    <p class="bio">Ethan is a Grade 10 student at Abbey Park High School in Oakville. With 2 years of competitive debate experience, he has advanced at prestigious tournaments such as Harvard WSDC, Queens BPHS, McGill BPHS, and Hart House High Schools.</p>
                </div>
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Rwei1.png" alt="Rachel Wei" onerror="this.style.display='none'">
                    </div>
                    <h3>Rachel Wei</h3>
                    <span class="role">Coquitlam Chapter Head</span>
                    <p class="bio">Rachel Wei is a rising senior at Port Moody Secondary School. She loves playing basketball, is an avid debater, and loves her pet cat! She is also a passionate environmentalist.</p>
                </div>
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Xyang1.jpg" alt="Xuhan Yang" onerror="this.style.display='none'">
                    </div>
                    <h3>Xuhan Yang</h3>
                    <span class="role">Director of Technology</span>
                    <p class="bio">Hi I'm Xuhan! I'm a high schooler passionate about programming, math, or anything STEM related!</p>
                </div>
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Chuan1.jpg" alt="Chloe Huang" onerror="this.style.display='none'">
                    </div>
                    <h3>Chloe Huang</h3>
                    <span class="role">Secretary</span>
                    <p class="bio">Chloe is a Grade 11 student at Earl of March High School. She is an avid volleyball player and loves sports!</p>
                </div>
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Kjosh1.png" alt="Keerti Joshi" onerror="this.style.display='none'">
                    </div>
                    <h3>Keerti Joshi</h3>
                    <span class="role">Debate Coach</span>
                    <p class="bio">I'm Keerti, I'm a grade 11 student at Upper Canada College. I've been debating since Grade 8 and I debate in both WSDC and BP formats. I am a new member of the Canadian National Debating Team.</p>
                </div>
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Kyip1.png" alt="Kristen Yip" onerror="this.style.display='none'">
                    </div>
                    <h3>Kristen Yip</h3>
                    <span class="role">Debate Coach</span>
                    <p class="bio">Kristen Y (she/her) is a grade 9 student and avid debater. Achievements include: Top 4th speaker+top jr speaker, top 3rd speaker + grand finalist, and grand finalist + 4th jr speaker.</p>
                </div>
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Czhan1.png" alt="Cody Zhang" onerror="this.style.display='none'">
                    </div>
                    <h3>Cody Zhang</h3>
                    <span class="role">Economics Instructor</span>
                    <p class="bio">Cody Zhang is a high schooler from Toronto and scored a 5 on AP Micro and makes economics simple, fun, and engaging!</p>
                </div>
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Jliu1.png" alt="Jeffrey Liu" onerror="this.style.display='none'">
                    </div>
                    <h3>Jeffrey Liu</h3>
                    <span class="role">Debate Coach</span>
                    <p class="bio">Hi, i'm Jeffery! i am a grade 11 student at milliken Mills high school. In my free time i love cooking food, listening to music, and working out!</p>
                </div>
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Aliu1.png" alt="Amy Liu" onerror="this.style.display='none'">
                    </div>
                    <h3>Amy Liu</h3>
                    <span class="role">Debate Coach</span>
                    <p class="bio">Amy is a G10 student and a competitive debater who has won many debate tournaments.</p>
                </div>
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Fzhan1.jpg" alt="Ferrari Zhang" onerror="this.style.display='none'">
                    </div>
                    <h3>Ferrari Zhang</h3>
                    <span class="role">Debate Coach</span>
                    <p class="bio">Ferrari is a G10 student and a competitive debater, who loves argumentation and refutation!</p>
                </div>
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Tguo1.png" alt="Terrence Guo" onerror="this.style.display='none'">
                    </div>
                    <h3>Terrence Guo</h3>
                    <span class="role">Debate Coach</span>
                    <p class="bio">Terrence is a G12 student and a competitive debater at the national level, winning many debating tournaments.</p>
                </div>
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Yshua1.png" alt="Yunfei Shuai" onerror="this.style.display='none'">
                    </div>
                    <h3>Yunfei Shuai</h3>
                    <span class="role">Contests Organizer</span>
                    <p class="bio">Yunfei wrote her first story when she was 7 years old and never looked back since. She is an avid sci-fi enthusiast and an aspiring astrophysicist.</p>
                </div>
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Szhen1.png" alt="Susan Zheng" onerror="this.style.display='none'">
                    </div>
                    <h3>Susan Zheng</h3>
                    <span class="role">Contests Organizer</span>
                    <p class="bio">Susan finds way too much enjoyment in daydreaming about fictional scenarios. A sci-fi fanatic, she obsesses over very specific mathematical and scientific concepts.</p>
                </div>
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Sisla1.png" alt="Shahrad Islam" onerror="this.style.display='none'">
                    </div>
                    <h3>Shahrad Islam</h3>
                    <span class="role">Science Instructor</span>
                    <p class="bio">Hi! My name is Shahrad! Some things you should know about me are that I like playing sports, playing instruments, watching movies and shows, and I really like cats!</p>
                </div>
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="https://www.nexyouth.org/Member_Rliu1.png" alt="Ronnie Liu" onerror="this.style.display='none'">
                    </div>
                    <h3>Ronnie Liu</h3>
                    <span class="role">Science Instructor</span>
                    <p class="bio">Hello, my name is Ronnie Liu. I am a gifted grade 10 scholar at Richmond Hill High School and I graduated with honors at Crosby Heights.</p>
                </div>
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="/AaronYang.jpg" alt="Aaron Yang" onerror="this.style.display='none'">
                    </div>
                    <h3>Aaron Yang</h3>
                    <span class="role">Team Member</span>
                    <p class="bio">Aaron is a dedicated member of the NexYouth team passionate about empowering youth and creating meaningful educational opportunities.</p>
                </div>
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="/VincentPham.jpg" alt="Vincent Pham" onerror="this.style.display='none'">
                    </div>
                    <h3>Vincent Pham</h3>
                    <span class="role">Team Member</span>
                    <p class="bio">Vincent is a committed volunteer with NexYouth who believes in the power of youth to create positive change and make a difference in their communities.</p>
                </div>
                <div class="team-member">
                    <div class="team-member-image">
                        <img src="/WilliamWang.jpg" alt="William Wang" onerror="this.style.display='none'">
                    </div>
                    <h3>William Wang</h3>
                    <span class="role">Team Member</span>
                    <p class="bio">William is an enthusiastic member of the NexYouth community committed to fostering growth and leadership among young people.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="community-section">
        <div class="container" style="text-align: center;">
            <h2>Join Our Community</h2>
            <p style="font-size: 1.1rem; color: rgba(255, 255, 255, 0.9); margin-bottom: 2rem;">Become part of a global movement of empowered youth changemakers.</p>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform" class="cta-btn">Get Involved</a>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2025 NexYouth. All rights reserved. | Grow • Lead • Act</p>
        </div>
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HOME_TEMPLATE)

@app.route('/partner')
def partner():
    return render_template_string(PARTNER_TEMPLATE)

@app.route('/about')
def about():
    return render_template_string(ABOUT_TEMPLATE)

@app.route('/<path:path>')
def catch_all(path):
    """Serve all other paths with the main HTML (for client-side routing)"""
    return render_template_string(HOME_TEMPLATE)

@app.errorhandler(404)
def not_found(e):
    return render_template_string(HOME_TEMPLATE), 200
