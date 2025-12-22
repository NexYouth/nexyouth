from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__, static_folder='public', static_url_path='/static')

@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serve static files from public folder"""
    return send_from_directory(os.path.join(os.path.dirname(__file__), 'public'), filename)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="NexYouth - Empowering youth globally through skill development and mentorship.">
    <title>NexYouth - Empowering Youth</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
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
            padding: 1.5rem 2rem;
        }

        nav .container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        nav .logo {
            font-size: 1.2rem;
            font-weight: 700;
            color: #000;
            text-decoration: none;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        nav a {
            text-decoration: none;
            color: #666;
            font-size: 0.9rem;
            transition: color 0.2s;
        }

        nav a:hover {
            color: #000;
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
            <a href="#home" class="logo">NexYouth</a>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#what-we-do">What We Do</a></li>
                <li><a href="#programs">Programs</a></li>
                <li><a href="#community">Community</a></li>
                <li><a href="#contact">Contact</a></li>
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
            <p>&copy; 2025 NexYouth. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/<path:path>')
def catch_all(path):
    """Catch all routes and return the main page for client-side routing"""
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

# WSGI entry point for Vercel
app = app
