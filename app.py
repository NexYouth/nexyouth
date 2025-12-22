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
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
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
    }

    nav .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 1.5rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    nav .logo {
        font-size: 1.3rem;
        font-weight: 600;
        color: #000;
        letter-spacing: 0.5px;
    }

    nav ul {
        display: flex;
        list-style: none;
        gap: 2.5rem;
    }

    nav a {
        text-decoration: none;
        color: #666;
        font-size: 0.95rem;
        transition: color 0.2s ease;
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
        min-height: 80vh;
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
        background: rgba(0, 0, 0, 0.4);
        z-index: 1;
    }

    .hero video {
        position: absolute;
        top: 50%;
        left: 50%;
        min-width: 100%;
        min-height: 100%;
        transform: translate(-50%, -50%);
        object-fit: cover;
        z-index: 0;
    }

    .hero .container {
        position: relative;
        z-index: 2;
    }

    .hero h1 {
        font-size: 3.5rem;
        margin-bottom: 1rem;
        font-weight: 700;
    }

    .hero p {
        font-size: 1.25rem;
        margin-bottom: 2rem;
        opacity: 0.95;
    }

    .cta-button {
        display: inline-block;
        background: #ff6b35;
        color: white;
        padding: 0.75rem 2rem;
        border-radius: 5px;
        text-decoration: none;
        transition: background 0.3s ease;
        font-weight: 600;
    }

    .cta-button:hover {
        background: #ff5520;
    }

    /* About Section */
    .about {
        padding: 5rem 2rem;
        background: #f9f9f9;
    }

    .about h2 {
        font-size: 2.5rem;
        margin-bottom: 2rem;
        text-align: center;
        color: #000;
    }

    .about-content {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 3rem;
        align-items: center;
    }

    .about-text h3 {
        font-size: 1.5rem;
        margin-bottom: 1rem;
        color: #000;
    }

    .about-text p {
        margin-bottom: 1rem;
        color: #666;
        line-height: 1.8;
    }

    .about-features {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }

    .feature-item {
        display: flex;
        gap: 1rem;
    }

    .feature-icon {
        font-size: 2rem;
        flex-shrink: 0;
    }

    .feature-text h4 {
        font-size: 1.1rem;
        margin-bottom: 0.25rem;
    }

    /* Events Section */
    .events {
        padding: 5rem 2rem;
    }

    .events h2 {
        font-size: 2.5rem;
        margin-bottom: 3rem;
        text-align: center;
    }

    .events-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
    }

    .event-card {
        background: white;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .event-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }

    .event-card img {
        width: 100%;
        height: 200px;
        object-fit: cover;
    }

    .event-card-content {
        padding: 1.5rem;
    }

    .event-card-content h3 {
        font-size: 1.25rem;
        margin-bottom: 0.75rem;
    }

    .event-card-content p {
        color: #666;
        font-size: 0.95rem;
    }

    /* Testimonials Section */
    .testimonials {
        padding: 5rem 2rem;
        background: #f9f9f9;
    }

    .testimonials h2 {
        font-size: 2.5rem;
        margin-bottom: 3rem;
        text-align: center;
    }

    .testimonials-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
    }

    .testimonial-card {
        background: white;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }

    .testimonial-text {
        font-style: italic;
        margin-bottom: 1.5rem;
        color: #666;
        line-height: 1.8;
    }

    .testimonial-author {
        font-weight: 600;
        margin-bottom: 0.25rem;
    }

    .testimonial-title {
        font-size: 0.9rem;
        color: #999;
    }

    /* Footer */
    footer {
        background: #000;
        color: white;
        padding: 3rem 2rem;
        text-align: center;
    }

    footer .links {
        margin-bottom: 1.5rem;
        display: flex;
        justify-content: center;
        gap: 2rem;
    }

    footer a {
        color: #fff;
        text-decoration: none;
        transition: color 0.3s ease;
    }

    footer a:hover {
        color: #ff6b35;
    }

    footer p {
        color: #999;
        font-size: 0.9rem;
    }

    @media (max-width: 768px) {
        .about-content {
            grid-template-columns: 1fr;
        }

        .hero h1 {
            font-size: 2rem;
        }

        nav ul {
            gap: 1.5rem;
        }
    }
        </style>
    </head>
    <body>
        <!-- Navigation -->
        <nav>
            <div class="container">
                <div class="logo">NexYouth</div>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#programs">Programs</a></li>
                    <li><a href="#testimonials">Testimonials</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </div>
        </nav>

        <!-- Hero Section -->
        <section id="home" class="hero">
            <video autoplay muted loop>
                <source src="/static/main_background.mp4" type="video/mp4">
                Your browser does not support the video tag.
            </video>
            <div class="container">
                <h1>Empower Your Future</h1>
                <p>Join a global community of youth empowering themselves through skill development and mentorship</p>
                <a href="#programs" class="cta-button">Explore Programs</a>
            </div>
        </section>

        <!-- About Section -->
        <section id="about" class="about">
            <div class="container">
                <h2>About NexYouth</h2>
                <div class="about-content">
                    <div class="about-text">
                        <h3>Who We Are</h3>
                        <p>NexYouth is a global organization dedicated to empowering young people with the skills, knowledge, and mentorship they need to succeed in an ever-changing world.</p>
                        <p>We believe that every young person deserves access to quality education, guidance, and opportunities. Our mission is to bridge the gap between education and employment by providing practical, industry-relevant skills and mentorship.</p>
                    </div>
                    <div class="about-features">
                        <div class="feature-item">
                            <div class="feature-icon">🎓</div>
                            <div class="feature-text">
                                <h4>Expert-Led Training</h4>
                                <p>Learn from industry professionals and experienced mentors</p>
                            </div>
                        </div>
                        <div class="feature-item">
                            <div class="feature-icon">🌍</div>
                            <div class="feature-text">
                                <h4>Global Community</h4>
                                <p>Connect with youth from around the world</p>
                            </div>
                        </div>
                        <div class="feature-item">
                            <div class="feature-icon">💼</div>
                            <div class="feature-text">
                                <h4>Career Support</h4>
                                <p>Get guidance on career development and opportunities</p>
                            </div>
                        </div>
                        <div class="feature-item">
                            <div class="feature-icon">🚀</div>
                            <div class="feature-text">
                                <h4>Innovation Focus</h4>
                                <p>Learn cutting-edge skills for the future</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Programs Section -->
        <section id="programs" class="events">
            <div class="container">
                <h2>Featured Programs & Events.</h2>
                <div class="events-grid">
                    <div class="event-card">
                        <img src="https://via.placeholder.com/400x200?text=Skill+Development" alt="Skill Development Courses">
                        <div class="event-card-content">
                            <h3>Skill Development Courses</h3>
                            <p>Comprehensive training programs designed to equip youth with in-demand skills. From digital literacy to entrepreneurship, our courses prepare students for real-world success.</p>
                        </div>
                    </div>
                    <div class="event-card">
                        <img src="https://via.placeholder.com/400x200?text=Expert+Seminars" alt="Expert Seminars">
                        <div class="event-card-content">
                            <h3>Expert Seminars & Talks</h3>
                            <p>Learn directly from industry leaders and experienced professionals. Our seminars provide insights into emerging opportunities and inspire the next generation of innovators.</p>
                        </div>
                    </div>
                    <div class="event-card">
                        <img src="https://via.placeholder.com/400x200?text=Competitions" alt="Competitions">
                        <div class="event-card-content">
                            <h3>Competitions & Contests</h3>
                            <p>Showcase your talent and compete with peers from around the globe. Our competitions recognize excellence and provide opportunities for networking and growth.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Testimonials Section -->
        <section id="testimonials" class="testimonials">
            <div class="container">
                <h2>Words From Our Community.</h2>
                <div class="testimonials-grid">
                    <div class="testimonial-card">
                        <div class="testimonial-text">"NexYouth completely transformed my perspective on personal development. The mentorship I received helped me navigate challenges and achieve my goals."</div>
                        <div class="testimonial-author">Sarah Johnson</div>
                        <div class="testimonial-title">Course Participant</div>
                    </div>
                    <div class="testimonial-card">
                        <div class="testimonial-text">"Being part of this community showed me that I'm not alone in my journey. The support and guidance from mentors made all the difference in my success."</div>
                        <div class="testimonial-author">Marcus Chen</div>
                        <div class="testimonial-title">Program Graduate</div>
                    </div>
                    <div class="testimonial-card">
                        <div class="testimonial-text">"The practical skills and confidence I gained through NexYouth's programs have been instrumental in landing my dream internship and building my career."</div>
                        <div class="testimonial-author">Amina Patel</div>
                        <div class="testimonial-title">Scholarship Winner</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Footer -->
        <footer id="contact">
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
