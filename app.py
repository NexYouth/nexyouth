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
            display: flex;
            align-items: center;
            text-decoration: none;
        }

        nav .logo img {
            height: 50px;
            width: auto;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        nav a {
            text-decoration: none;
            color: #333;
            font-size: 1.2rem;
            font-weight: 600;
            transition: color 0.2s;
            text-transform: uppercase;
            letter-spacing: 1px;
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
            <a href="/" class="logo">
                <img src="/static/logo.svg" alt="NexYouth">
            </a>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/#what-we-do">What We Do</a></li>
                <li><a href="/#programs">Programs</a></li>
                <li><a href="/#community">Community</a></li>
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
            display: flex;
            align-items: center;
            text-decoration: none;
        }

        nav .logo img {
            height: 50px;
            width: auto;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        nav a {
            text-decoration: none;
            color: #333;
            font-size: 1.2rem;
            font-weight: 600;
            transition: color 0.2s;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        nav a:hover {
            color: #000;
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
                <li><a href="/about">About</a></li>
                <li><a href="/#what-we-do">What We Do</a></li>
                <li><a href="/#programs">Programs</a></li>
                <li><a href="/#community">Community</a></li>
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
                        <p>Justin is an enthusiast of the environment. He is an avid reader of all forms of media related to the environment. He hopes that through this contest, others will also find their own love and passion for one of the largest global issues in the world.</p>
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
                        <div class="team-role">Canada Head & Director of Operations</div>
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
                        <div class="team-role">Coquitlam Chapter Head</div>
                        <h3>Rachel Wei</h3>
                        <p>Rachel Wei is a rising senior at Port Moody Secondary School. She loves playing basketball, is an avid debater, and loves her pet cat! She is also a passionate environmentalist.</p>
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

                <!-- Keerti Joshi -->
                <div class="team-card">
                    <img src="https://www.nexyouth.org/Member_Kjosh1.png" alt="Keerti Joshi">
                    <div class="team-card-content">
                        <div class="team-role">Debate Coach</div>
                        <h3>Keerti Joshi</h3>
                        <p>I'm Keerti, I'm a grade 11 student at Upper Canada College. I've been debating since Grade 8 and I debate in both WSDC and BP formats. I am a new member of the Canadian National Debating Team and have competed and won in many tournaments run by Canadian Universities.</p>
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

                <!-- Ethan Luo -->
                <div class="team-card">
                    <img src="https://www.nexyouth.org/Member_Eluo1.png" alt="Ethan Luo">
                    <div class="team-card-content">
                        <div class="team-role">Debate Coach</div>
                        <h3>Ethan Luo</h3>
                        <p>Ethan is a Grade 10 student at Abbey Park High School in Oakville. With 2 years of competitive debate experience, he has advanced at prestigious tournaments such as Harvard WSDC, Queens BPHS, McGill BPHS, and Hart House High Schools. Outside debate, he enjoys clarinet, trail running, and co-hosting Perception Podcast.</p>
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
            <p>&copy; 2025 NexYouth. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

@app.route('/about')
def about():
    return render_template_string(ABOUT_TEMPLATE)

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
