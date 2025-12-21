from flask import Flask

app = Flask(__name__)

# CSS Styles
styles = """
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
        width: auto;
        height: auto;
        transform: translate(-50%, -50%);
        z-index: 0;
        object-fit: cover;
    }

    .hero > div {
        position: relative;
        z-index: 2;
    }
    
    .hero h1 {
        text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
    }
    
    .hero p {
        text-shadow: 1px 1px 4px rgba(0,0,0,0.5);
    }
    
    .hero-button {
        background: #000 !important;
        color: white !important;
    }
    
    .hero-button:hover {
        background: #333 !important;
    }

    .hero h1 {
        font-size: 3.5rem;
        margin-bottom: 1rem;
        font-weight: 700;
        line-height: 1.2;
    }

    .hero p {
        font-size: 1.1rem;
        max-width: 700px;
        margin: 0 auto 2rem;
        color: #fff;
        line-height: 1.7;
    }

    .hero-button {
        display: inline-block;
        background: #000;
        color: white;
        padding: 0.8rem 2.5rem;
        border: none;
        border-radius: 4px;
        font-weight: 600;
        cursor: pointer;
        text-decoration: none;
        transition: background 0.3s ease;
        font-size: 0.95rem;
    }

    .hero-button:hover {
        background: #333;
    }

    /* What We Do Section */
    .what-we-do {
        padding: 6rem 0;
        background: white;
        text-align: center;
    }

    .what-we-do h2 {
        font-size: 2.5rem;
        margin-bottom: 2rem;
        font-weight: 700;
    }

    .what-we-do-content {
        max-width: 700px;
        margin: 0 auto 2rem;
        font-size: 1.05rem;
        color: #666;
        line-height: 1.8;
    }

    .links {
        display: flex;
        gap: 2rem;
        justify-content: center;
        flex-wrap: wrap;
    }

    .links a {
        text-decoration: none;
        color: #000;
        font-weight: 600;
        border-bottom: 2px solid #000;
        padding-bottom: 0.3rem;
        transition: opacity 0.3s ease;
    }

    .links a:hover {
        opacity: 0.6;
    }

    /* Featured Events Section */
    .featured-events {
        padding: 6rem 0;
        background: #f8f8f8;
    }

    .featured-events h2 {
        font-size: 2.5rem;
        margin-bottom: 3rem;
        font-weight: 700;
        text-align: center;
    }

    .events-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 2.5rem;
    }

    .event-card {
        background: white;
        border-radius: 8px;
        overflow: hidden;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .event-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }

    .event-card img {
        width: 100%;
        height: 200px;
        object-fit: cover;
    }

    .event-card-content {
        padding: 2rem;
    }

    .event-card h3 {
        font-size: 1.4rem;
        margin-bottom: 1rem;
        font-weight: 600;
    }

    .event-card p {
        color: #666;
        font-size: 0.95rem;
        line-height: 1.7;
    }

    /* Testimonials Section */
    .testimonials {
        padding: 6rem 0;
        background: white;
    }

    .testimonials h2 {
        font-size: 2.5rem;
        margin-bottom: 3rem;
        font-weight: 700;
        text-align: center;
    }

    .testimonials-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
    }

    .testimonial-card {
        background: #f8f8f8;
        padding: 2rem;
        border-radius: 8px;
        border-left: 4px solid #000;
    }

    .testimonial-text {
        color: #666;
        font-size: 0.95rem;
        line-height: 1.8;
        margin-bottom: 1.5rem;
        font-style: italic;
    }

    .testimonial-author {
        font-weight: 600;
        color: #000;
        font-size: 0.9rem;
    }

    .testimonial-title {
        color: #999;
        font-size: 0.85rem;
        margin-top: 0.5rem;
    }

    /* Footer */
    footer {
        background: #000;
        color: white;
        padding: 3rem 0;
        text-align: center;
    }

    footer .links {
        margin-bottom: 2rem;
        justify-content: center;
    }

    footer .links a {
        color: white;
        border-bottom-color: white;
    }

    footer p {
        font-size: 0.9rem;
        color: #999;
    }

    /* Responsive */
    @media (max-width: 768px) {
        nav ul {
            gap: 1.5rem;
            font-size: 0.85rem;
        }

        .hero h1 {
            font-size: 2rem;
        }

        .what-we-do h2,
        .featured-events h2,
        .testimonials h2 {
            font-size: 1.8rem;
        }

        .links {
            flex-direction: column;
            gap: 1rem;
        }

        .events-grid {
            grid-template-columns: 1fr;
        }
    }
"""

@app.route("/")
def home():
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="NexYouth - Empowering youth globally through skill development and mentorship.">
        <title>NexYouth - Empowering Youth</title>
        <style>
            {styles}
        </style>
    </head>
    <body>
        <!-- Navigation -->
        <nav>
            <div class="container">
                <div class="logo">NexYouth</div>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#stats">Impact</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </div>
        </nav>

        <!-- Hero Section -->
        <section id="home" class="hero">
            <video autoplay muted loop playsinline>
                <source src="https://media.istockphoto.com/id/1369850776/video/business-people-in-the-office.mp4?s=mp4-640x640-is" type="video/mp4">
            </video>
            <div>
                <h1>Empowering youth to build the future.</h1>
                <p>A government-accredited NGO dedicated to fostering positive change through skill development, mentorship, and community building.</p>
                <a href="#what-we-do" class="hero-button">Learn More</a>
            </div>
        </section>

        <!-- What We Do Section -->
        <section id="what-we-do" class="what-we-do">
            <div class="container">
                <h2>What We Do.</h2>
                <div class="what-we-do-content">
                    <p>Here at NexYouth, we are on a mission to empower youth through high-quality education, hands-on training, and meaningful mentorship. We create inclusive communities where young people can develop skills, explore opportunities, and become the changemakers of tomorrow.</p>
                </div>
                <div class="links">
                    <a href="#featured">Featured Events</a>
                    <a href="#testimonials">Our Community</a>
                    <a href="#contact">Get Involved</a>
                </div>
            </div>
        </section>

        <!-- Featured Events Section -->
        <section id="featured" class="featured-events">
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
    return html

if __name__ == "__main__":
    app.run(debug=True, port=8000)
