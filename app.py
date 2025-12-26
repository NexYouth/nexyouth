from flask import Flask, render_template_string

app = Flask(__name__, static_folder='public', static_url_path='/static')

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NexYouth - Empowering the Next Generation</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #0891b2;
            --primary-dark: #0e7490;
            --secondary: #f97316;
            --dark: #f8fafc;
            --darker: #ffffff;
            --light: #1e293b;
            --gray: #64748b;
            --gradient: linear-gradient(135deg, #0891b2 0%, #06b6d4 100%);
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background: var(--darker);
            color: var(--light);
            line-height: 1.6;
            overflow-x: hidden;
        }

        /* Navigation */
        nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            padding: 1rem 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
            border-bottom: 1px solid #e2e8f0;
        }

        nav.scrolled {
            padding: 0.8rem 5%;
            box-shadow: 0 2px 20px rgba(0, 0, 0, 0.08);
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 10px;
            text-decoration: none;
        }

        .logo img {
            height: 45px;
        }

        .nav-links {
            display: flex;
            gap: 2.5rem;
            list-style: none;
            align-items: center;
        }

        .nav-links a {
            color: var(--light);
            text-decoration: none;
            font-weight: 500;
            font-size: 0.95rem;
            transition: color 0.3s ease;
            position: relative;
        }

        .nav-links a:hover {
            color: var(--primary);
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--primary);
            transition: width 0.3s ease;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        .nav-btn {
            background: var(--gradient);
            color: var(--dark);
            padding: 0.7rem 1.8rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .nav-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(0, 212, 255, 0.4);
        }

        .nav-btn::after {
            display: none;
        }

        /* Hero Section */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
            padding: 100px 5% 60px;
        }

        .hero-bg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
        }

        .hero-bg video {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .hero-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: transparent;
            z-index: -1;
        }

        .hero-content {
            text-align: center;
            max-width: 900px;
        }

        .hero h1 {
            font-size: 4rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            line-height: 1.1;
            color: #0f172a;
            text-shadow: 1px 1px 2px rgba(255,255,255,0.8), -1px -1px 2px rgba(255,255,255,0.8), 1px -1px 2px rgba(255,255,255,0.8), -1px 1px 2px rgba(255,255,255,0.8);
        }

        .hero p {
            font-size: 1.3rem;
            color: #334155;
            margin-bottom: 2.5rem;
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
            text-shadow: 1px 1px 2px rgba(255,255,255,0.8), -1px -1px 2px rgba(255,255,255,0.8);
        }

        .hero-btns {
            display: flex;
            gap: 1.5rem;
            justify-content: center;
            flex-wrap: wrap;
        }

        .btn-primary {
            background: var(--gradient);
            color: #ffffff;
            padding: 1rem 2.5rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            font-size: 1.1rem;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 10px;
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(8, 145, 178, 0.4);
        }

        .btn-secondary {
            background: transparent;
            color: var(--light);
            padding: 1rem 2.5rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            font-size: 1.1rem;
            border: 2px solid var(--primary);
            transition: all 0.3s ease;
        }

        .btn-secondary:hover {
            background: var(--primary);
            color: var(--dark);
        }

        /* Section Styles */
        section {
            padding: 100px 5%;
        }

        .section-header {
            text-align: center;
            margin-bottom: 60px;
        }

        .section-header h2 {
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 1rem;
            color: var(--light);
        }

        .section-header p {
            color: var(--gray);
            font-size: 1.2rem;
            max-width: 600px;
            margin: 0 auto;
        }

        /* Featured Section (like COP30 section) */
        .featured-section {
            background: linear-gradient(180deg, var(--darker) 0%, var(--dark) 100%);
        }

        .featured-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .featured-card {
            background: #ffffff;
            border-radius: 20px;
            overflow: hidden;
            transition: all 0.4s ease;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        }

        .featured-card:hover {
            transform: translateY(-10px);
            border-color: var(--primary);
            box-shadow: 0 20px 40px rgba(8, 145, 178, 0.15);
        }

        .featured-card img {
            width: 100%;
            height: 250px;
            object-fit: cover;
        }

        .featured-card-content {
            padding: 1.5rem;
        }

        .featured-card h3 {
            font-size: 1.3rem;
            margin-bottom: 0.8rem;
            color: var(--light);
        }

        .featured-card p {
            color: var(--gray);
            font-size: 0.95rem;
            margin-bottom: 1rem;
        }

        .featured-card a {
            color: var(--primary);
            text-decoration: none;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            transition: gap 0.3s ease;
        }

        .featured-card a:hover {
            gap: 10px;
        }

        /* Mission Section */
        .mission-section {
            background: var(--dark);
            position: relative;
        }

        .mission-content {
            max-width: 1000px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            align-items: center;
        }

        .mission-text h3 {
            color: var(--primary);
            font-size: 1rem;
            text-transform: uppercase;
            letter-spacing: 3px;
            margin-bottom: 1rem;
        }

        .mission-text h2 {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            color: var(--light);
        }

        .mission-text p {
            color: var(--gray);
            font-size: 1.1rem;
            line-height: 1.8;
        }

        .mission-image {
            position: relative;
        }

        .mission-image img {
            width: 100%;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        }

        .mission-image::before {
            content: '';
            position: absolute;
            top: -20px;
            right: -20px;
            width: 100%;
            height: 100%;
            border: 3px solid var(--primary);
            border-radius: 20px;
            z-index: -1;
        }

        /* Stats Section */
        .stats-section {
            background: var(--gradient);
            padding: 60px 5%;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .stat-item {
            text-align: center;
        }

        .stat-number {
            font-size: 3.5rem;
            font-weight: 800;
            color: #ffffff;
        }

        .stat-label {
            font-size: 1rem;
            color: #ffffff;
            font-weight: 500;
            opacity: 0.9;
        }

        /* Partners Section */
        .partners-section {
            background: var(--darker);
            overflow: hidden;
        }

        .partners-scroll {
            display: flex;
            animation: scroll 30s linear infinite;
            width: calc(200px * 12);
        }

        .partners-scroll:hover {
            animation-play-state: paused;
        }

        @keyframes scroll {
            0% {
                transform: translateX(0);
            }
            100% {
                transform: translateX(calc(-200px * 6));
            }
        }

        .partner-logo {
            flex: 0 0 200px;
            height: 100px;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 0 2rem;
            filter: grayscale(100%) brightness(0.8);
            opacity: 0.6;
            transition: all 0.3s ease;
        }

        .partner-logo:hover {
            filter: grayscale(0%) brightness(1);
            opacity: 1;
        }

        .partner-logo img {
            max-width: 100%;
            max-height: 60px;
        }

        /* Events Section */
        .events-section {
            background: linear-gradient(180deg, var(--dark) 0%, var(--darker) 100%);
        }

        .events-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            max-width: 1400px;
            margin: 0 auto;
        }

        .event-card {
            background: #ffffff;
            border-radius: 20px;
            overflow: hidden;
            border: 1px solid #e2e8f0;
            transition: all 0.4s ease;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        }

        .event-card:hover {
            transform: translateY(-5px);
            border-color: var(--primary);
            box-shadow: 0 10px 30px rgba(8, 145, 178, 0.15);
        }

        .event-image {
            position: relative;
            height: 200px;
            overflow: hidden;
        }

        .event-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.4s ease;
        }

        .event-card:hover .event-image img {
            transform: scale(1.05);
        }

        .event-date {
            position: absolute;
            top: 15px;
            left: 15px;
            background: var(--primary);
            color: var(--dark);
            padding: 0.5rem 1rem;
            border-radius: 10px;
            text-align: center;
            font-weight: 700;
        }

        .event-date .day {
            font-size: 1.5rem;
            line-height: 1;
        }

        .event-date .month {
            font-size: 0.75rem;
            text-transform: uppercase;
        }

        .event-content {
            padding: 1.5rem;
        }

        .event-content h3 {
            font-size: 1.2rem;
            margin-bottom: 0.5rem;
            color: var(--light);
        }

        .event-content .event-time {
            color: var(--primary);
            font-size: 0.85rem;
            margin-bottom: 0.8rem;
        }

        .event-content p {
            color: var(--gray);
            font-size: 0.9rem;
            margin-bottom: 1rem;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }

        .event-link {
            color: var(--primary);
            text-decoration: none;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            font-size: 0.9rem;
        }

        .event-link:hover {
            gap: 10px;
        }

        /* News Section */
        .news-section {
            background: var(--darker);
        }

        .news-slider {
            display: flex;
            gap: 2rem;
            overflow-x: auto;
            padding: 1rem 0;
            scroll-snap-type: x mandatory;
            -webkit-overflow-scrolling: touch;
            max-width: 1400px;
            margin: 0 auto;
        }

        .news-slider::-webkit-scrollbar {
            height: 8px;
        }

        .news-slider::-webkit-scrollbar-track {
            background: #e2e8f0;
            border-radius: 10px;
        }

        .news-slider::-webkit-scrollbar-thumb {
            background: var(--primary);
            border-radius: 10px;
        }

        .news-card {
            flex: 0 0 350px;
            scroll-snap-align: start;
            background: #ffffff;
            border-radius: 15px;
            overflow: hidden;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        }

        .news-card img {
            width: 100%;
            height: 180px;
            object-fit: cover;
        }

        .news-card-content {
            padding: 1.2rem;
        }

        .news-card-content .date {
            color: var(--primary);
            font-size: 0.85rem;
            margin-bottom: 0.5rem;
        }

        .news-card-content h4 {
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
            color: var(--light);
        }

        .news-card-content p {
            color: var(--gray);
            font-size: 0.9rem;
        }

        /* CTA Section */
        .cta-section {
            background: linear-gradient(135deg, #0891b2 0%, #06b6d4 100%);
            text-align: center;
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
            background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.1'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
            opacity: 0.5;
        }

        .cta-content {
            position: relative;
            z-index: 1;
        }

        .cta-section h2 {
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            color: #ffffff;
        }

        .cta-section h2 span {
            color: #ffffff;
        }

        .cta-section p {
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.2rem;
            margin-bottom: 2rem;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }

        /* Footer */
        footer {
            background: #1e293b;
            padding: 80px 5% 30px;
            border-top: 1px solid #334155;
        }

        .footer-content {
            display: grid;
            grid-template-columns: 2fr 1fr 1fr 1fr;
            gap: 4rem;
            max-width: 1400px;
            margin: 0 auto 50px;
        }

        .footer-brand img {
            height: 50px;
            margin-bottom: 1.5rem;
        }

        .footer-brand p {
            color: #94a3b8;
            font-size: 0.95rem;
            line-height: 1.8;
            margin-bottom: 1.5rem;
        }

        .footer-social {
            display: flex;
            gap: 1rem;
        }

        .footer-social a {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.15);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #ffffff;
            text-decoration: none;
            transition: all 0.3s ease;
        }

        .footer-social a:hover {
            background: var(--primary);
            color: #ffffff;
        }

        .footer-links h4 {
            font-size: 1.1rem;
            margin-bottom: 1.5rem;
            color: #ffffff;
        }

        .footer-links ul {
            list-style: none;
        }

        .footer-links li {
            margin-bottom: 0.8rem;
        }

        .footer-links a {
            color: #94a3b8;
            text-decoration: none;
            transition: color 0.3s ease;
        }

        .footer-links a:hover {
            color: var(--primary);
        }

        .footer-contact p {
            color: #94a3b8;
            margin-bottom: 0.5rem;
            font-size: 0.95rem;
        }

        .footer-bottom {
            text-align: center;
            padding-top: 30px;
            border-top: 1px solid #334155;
            color: #94a3b8;
            font-size: 0.9rem;
        }

        /* Mobile Menu */
        .mobile-menu-btn {
            display: none;
            flex-direction: column;
            gap: 5px;
            cursor: pointer;
            padding: 5px;
        }

        .mobile-menu-btn span {
            width: 25px;
            height: 2px;
            background: var(--light);
            transition: all 0.3s ease;
        }

        /* Responsive */
        @media (max-width: 1024px) {
            .hero h1 {
                font-size: 3rem;
            }

            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .mission-content {
                grid-template-columns: 1fr;
                gap: 3rem;
            }

            .mission-image::before {
                display: none;
            }

            .footer-content {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }

            .mobile-menu-btn {
                display: flex;
            }

            .hero h1 {
                font-size: 2.5rem;
            }

            .hero p {
                font-size: 1.1rem;
            }

            .section-header h2 {
                font-size: 2rem;
            }

            .stats-grid {
                grid-template-columns: 1fr 1fr;
                gap: 1.5rem;
            }

            .stat-number {
                font-size: 2.5rem;
            }

            .footer-content {
                grid-template-columns: 1fr;
                gap: 2rem;
            }

            .cta-section h2 {
                font-size: 2rem;
            }
        }

        @media (max-width: 480px) {
            .hero h1 {
                font-size: 2rem;
            }

            .hero-btns {
                flex-direction: column;
            }

            .stats-grid {
                grid-template-columns: 1fr 1fr;
            }
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav>
        <a href="/" class="logo">
            <img src="/static/logo.svg" alt="NexYouth Logo">
        </a>
        <ul class="nav-links">
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/#programs">Programs</a></li>
            <li><a href="/#events">Events</a></li>
            <li><a href="/#partners">Partners</a></li>
            <li><a href="/contact">Contact</a></li>
            <li><a href="mailto:nexyouth.master@gmail.com" class="nav-btn">Get Involved →</a></li>
        </ul>
        <div class="mobile-menu-btn">
            <span></span>
            <span></span>
            <span></span>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero" id="home">
        <div class="hero-bg">
            <video autoplay muted loop playsinline>
                <source src="/static/main_background.mp4" type="video/mp4">
            </video>
        </div>
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <h1>Empowering Youth to Lead Change</h1>
            <p>NexYouth connects young leaders with opportunities to develop skills, build community, and create meaningful impact across the globe.</p>
            <div class="hero-btns">
                <a href="mailto:nexyouth.master@gmail.com?subject=Get%20Involved" class="btn-primary">Take Action →</a>
                <a href="#about" class="btn-secondary">Learn More</a>
            </div>
        </div>
    </section>

    <!-- Featured Section -->
    <section class="featured-section" id="featured">
        <div class="section-header">
            <h2>NexYouth Highlights</h2>
            <p>See what we've been up to and where we're making an impact</p>
        </div>
        <div class="featured-grid">
            <div class="featured-card">
                <img src="https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=600" alt="Workshop">
                <div class="featured-card-content">
                    <h3>Public Speaking Workshops</h3>
                    <p>Partnering with CICS Immigrant Youth Centre to deliver workshops that help newcomer youth build confidence and self-expression.</p>
                    <a href="#programs">Learn More →</a>
                </div>
            </div>
            <div class="featured-card">
                <img src="https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=600" alt="Seminar">
                <div class="featured-card-content">
                    <h3>Expert-Led Seminars</h3>
                    <p>Monthly seminars featuring industry professionals sharing insights on leadership, entrepreneurship, and career development.</p>
                    <a href="#programs">Learn More →</a>
                </div>
            </div>
            <div class="featured-card">
                <img src="https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=600" alt="Mentorship">
                <div class="featured-card-content">
                    <h3>1-on-1 Mentorship Program</h3>
                    <p>Connecting youth with experienced mentors who provide guidance, support, and real-world advice for personal growth.</p>
                    <a href="#programs">Learn More →</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Mission Section -->
    <section class="mission-section" id="about">
        <div class="mission-content">
            <div class="mission-text">
                <h3>Our Mission</h3>
                <h2>Building the Next Generation of Leaders</h2>
                <p>NexYouth is committed to empowering youth through skill development programs, mentorship opportunities, and community engagement. We provide high school and college students with hands-on experiences in public speaking, leadership, and professional development. By nurturing a global community of changemakers, we aim to equip youth with the tools and experiences necessary to drive meaningful impact and build a brighter future.</p>
            </div>
            <div class="mission-image">
                <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600" alt="Team collaboration">
            </div>
        </div>
    </section>

    <!-- Stats Section -->
    <section class="stats-section">
        <div class="stats-grid">
            <div class="stat-item">
                <div class="stat-number">5000+</div>
                <div class="stat-label">Individuals Reached</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">90+</div>
                <div class="stat-label">Schools Engaged</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">13+</div>
                <div class="stat-label">Countries</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">700+</div>
                <div class="stat-label">Active Members</div>
            </div>
        </div>
    </section>

    <!-- Events Section -->
    <section class="events-section" id="events">
        <div class="section-header">
            <h2>Past Events</h2>
            <p>Explore our recent programs and community gatherings</p>
        </div>
        <div class="events-grid">
            <div class="event-card">
                <div class="event-image">
                    <img src="https://images.unsplash.com/photo-1475721027785-f74eccf877e2?w=600" alt="Public Speaking Workshop">
                    <div class="event-date">
                        <div class="day">15</div>
                        <div class="month">DEC</div>
                    </div>
                </div>
                <div class="event-content">
                    <h3>Public Speaking Workshop with CICS</h3>
                    <div class="event-time">SUNDAY, DECEMBER 15TH | 2PM – 4PM</div>
                    <p>An interactive workshop helping newcomer youth build confidence, voice, and self-expression through public speaking exercises.</p>
                    <a href="#" class="event-link">View More →</a>
                </div>
            </div>
            <div class="event-card">
                <div class="event-image">
                    <img src="https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=600" alt="Leadership Seminar">
                    <div class="event-date">
                        <div class="day">08</div>
                        <div class="month">DEC</div>
                    </div>
                </div>
                <div class="event-content">
                    <h3>Youth Leadership Seminar</h3>
                    <div class="event-time">SUNDAY, DECEMBER 8TH | 10AM – 12PM</div>
                    <p>Industry experts shared insights on developing leadership skills and creating impact in your community and beyond.</p>
                    <a href="#" class="event-link">View More →</a>
                </div>
            </div>
            <div class="event-card">
                <div class="event-image">
                    <img src="https://images.unsplash.com/photo-1528605248644-14dd04022da1?w=600" alt="Networking Event">
                    <div class="event-date">
                        <div class="day">24</div>
                        <div class="month">NOV</div>
                    </div>
                </div>
                <div class="event-content">
                    <h3>Community Networking Night</h3>
                    <div class="event-time">SATURDAY, NOVEMBER 24TH | 6PM – 8PM</div>
                    <p>A chance for NexYouth members to connect, share experiences, and build meaningful relationships with fellow youth leaders.</p>
                    <a href="#" class="event-link">View More →</a>
                </div>
            </div>
            <div class="event-card">
                <div class="event-image">
                    <img src="https://images.unsplash.com/photo-1515187029135-18ee286d815b?w=600" alt="Mentorship Launch">
                    <div class="event-date">
                        <div class="day">10</div>
                        <div class="month">NOV</div>
                    </div>
                </div>
                <div class="event-content">
                    <h3>Mentorship Program Launch</h3>
                    <div class="event-time">SUNDAY, NOVEMBER 10TH | 3PM – 5PM</div>
                    <p>Official launch of our 1-on-1 mentorship program, connecting youth with experienced professionals across various industries.</p>
                    <a href="#" class="event-link">View More →</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Partners Section -->
    <section class="partners-section" id="partners">
        <div class="section-header">
            <h2>Our Partners</h2>
            <p>Working together to empower the next generation</p>
        </div>
        <div class="partners-scroll">
            <div class="partner-logo">
                <img src="https://via.placeholder.com/150x60/1a1a2e/00d4ff?text=CICS" alt="CICS">
            </div>
            <div class="partner-logo">
                <img src="https://via.placeholder.com/150x60/1a1a2e/00d4ff?text=Partner+2" alt="Partner">
            </div>
            <div class="partner-logo">
                <img src="https://via.placeholder.com/150x60/1a1a2e/00d4ff?text=Partner+3" alt="Partner">
            </div>
            <div class="partner-logo">
                <img src="https://via.placeholder.com/150x60/1a1a2e/00d4ff?text=Partner+4" alt="Partner">
            </div>
            <div class="partner-logo">
                <img src="https://via.placeholder.com/150x60/1a1a2e/00d4ff?text=Partner+5" alt="Partner">
            </div>
            <div class="partner-logo">
                <img src="https://via.placeholder.com/150x60/1a1a2e/00d4ff?text=Partner+6" alt="Partner">
            </div>
            <!-- Duplicate for seamless loop -->
            <div class="partner-logo">
                <img src="https://via.placeholder.com/150x60/1a1a2e/00d4ff?text=CICS" alt="CICS">
            </div>
            <div class="partner-logo">
                <img src="https://via.placeholder.com/150x60/1a1a2e/00d4ff?text=Partner+2" alt="Partner">
            </div>
            <div class="partner-logo">
                <img src="https://via.placeholder.com/150x60/1a1a2e/00d4ff?text=Partner+3" alt="Partner">
            </div>
            <div class="partner-logo">
                <img src="https://via.placeholder.com/150x60/1a1a2e/00d4ff?text=Partner+4" alt="Partner">
            </div>
            <div class="partner-logo">
                <img src="https://via.placeholder.com/150x60/1a1a2e/00d4ff?text=Partner+5" alt="Partner">
            </div>
            <div class="partner-logo">
                <img src="https://via.placeholder.com/150x60/1a1a2e/00d4ff?text=Partner+6" alt="Partner">
            </div>
        </div>
    </section>

    <!-- News Section -->
    <section class="news-section" id="news">
        <div class="section-header">
            <h2>NexYouth in the News</h2>
            <p>Latest updates and stories from our community</p>
        </div>
        <div class="news-slider">
            <div class="news-card">
                <img src="https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=600" alt="News">
                <div class="news-card-content">
                    <div class="date">December 2024</div>
                    <h4>NexYouth Partners with CICS for Newcomer Youth Programs</h4>
                    <p>Delivering public speaking workshops to help immigrant youth build confidence.</p>
                </div>
            </div>
            <div class="news-card">
                <img src="https://images.unsplash.com/photo-1557804506-669a67965ba0?w=600" alt="News">
                <div class="news-card-content">
                    <div class="date">November 2024</div>
                    <h4>5000+ Youth Reached Through Our Programs</h4>
                    <p>A milestone achievement in our mission to empower young leaders globally.</p>
                </div>
            </div>
            <div class="news-card">
                <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?w=600" alt="News">
                <div class="news-card-content">
                    <div class="date">October 2024</div>
                    <h4>Mentorship Program Expands to 13 Countries</h4>
                    <p>Our global network continues to grow with mentors from diverse industries.</p>
                </div>
            </div>
            <div class="news-card">
                <img src="https://images.unsplash.com/photo-1531482615713-2afd69097998?w=600" alt="News">
                <div class="news-card-content">
                    <div class="date">September 2024</div>
                    <h4>NexYouth Launches Skill Development Initiative</h4>
                    <p>New programs focused on practical skills for the modern workplace.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
        <div class="cta-content">
            <h2>Take Action for a <span>Brighter Future</span></h2>
            <p>Join our community of young leaders making a difference. Get involved today and start your journey.</p>
            <a href="mailto:nexyouth.master@gmail.com?subject=Get%20Involved" class="btn-primary">Get Involved →</a>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="footer-content">
            <div class="footer-brand">
                <img src="/static/logo.svg" alt="NexYouth Logo">
                <p>NexYouth is committed to empowering the next generation of leaders through skill development, mentorship, and community engagement.</p>
                <div class="footer-social">
                    <a href="https://www.instagram.com/nexyouth.ngo/" target="_blank">📷</a>
                    <a href="https://www.linkedin.com/company/nexyouth-society/" target="_blank">💼</a>
                    <a href="https://discord.com/invite/qqT2ce3NY7" target="_blank">💬</a>
                </div>
            </div>
            <div class="footer-links">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="#programs">Programs</a></li>
                    <li><a href="#events">Events</a></li>
                </ul>
            </div>
            <div class="footer-links">
                <h4>Programs</h4>
                <ul>
                    <li><a href="#">Skill Development</a></li>
                    <li><a href="#">Seminars</a></li>
                    <li><a href="#">Mentorship</a></li>
                    <li><a href="#">Workshops</a></li>
                </ul>
            </div>
            <div class="footer-links footer-contact">
                <h4>Contact Us</h4>
                <p>Toronto, Canada</p>
                <p>nexyouth.master@gmail.com</p>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2023 NexYouth. All Rights Reserved.</p>
        </div>
    </footer>

    <script>
        // Navbar scroll effect
        window.addEventListener('scroll', function() {
            const nav = document.querySelector('nav');
            if (window.scrollY > 50) {
                nav.classList.add('scrolled');
            } else {
                nav.classList.remove('scrolled');
            }
        });

        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    </script>
</body>
</html>
"""

CONTACT_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - NexYouth</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #0891b2;
            --primary-light: #22d3ee;
            --dark: #1e293b;
            --darker: #0f172a;
            --light: #f8fafc;
            --white: #ffffff;
            --gray: #64748b;
            --gray-light: #94a3b8;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background: var(--light);
            color: var(--dark);
            line-height: 1.6;
        }

        /* Navigation */
        nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            padding: 1rem 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        .logo img {
            height: 45px;
        }

        .nav-links {
            display: flex;
            gap: 2.5rem;
            list-style: none;
            align-items: center;
        }

        .nav-links a {
            color: var(--dark);
            text-decoration: none;
            font-weight: 500;
            font-size: 0.95rem;
            transition: color 0.3s ease;
        }

        .nav-links a:hover {
            color: var(--primary);
        }

        .nav-btn {
            background: var(--primary);
            color: var(--white);
            padding: 0.7rem 1.8rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .nav-btn:hover {
            background: var(--primary-light);
            transform: translateY(-2px);
        }

        /* Hero */
        .contact-hero {
            padding: 140px 5% 60px;
            text-align: center;
            background: var(--white);
        }

        .contact-hero span {
            color: var(--primary);
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 3px;
            font-weight: 600;
        }

        .contact-hero h1 {
            font-size: 3rem;
            font-weight: 700;
            color: var(--dark);
            margin-top: 0.5rem;
        }

        /* Main Content */
        .contact-main {
            max-width: 600px;
            margin: 0 auto;
            padding: 60px 5%;
        }

        /* Form */
        .contact-form h2 {
            font-size: 1.3rem;
            color: var(--dark);
            margin-bottom: 1.5rem;
            text-align: center;
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 1rem 1.2rem;
            border: 2px solid #e2e8f0;
            border-radius: 10px;
            font-family: 'Poppins', sans-serif;
            font-size: 1rem;
            background: var(--white);
            color: var(--dark);
            transition: all 0.3s ease;
        }

        .form-group input:focus,
        .form-group textarea:focus {
            outline: none;
            border-color: var(--primary);
        }

        .form-group input::placeholder,
        .form-group textarea::placeholder {
            color: var(--gray-light);
        }

        .form-group textarea {
            min-height: 150px;
            resize: vertical;
        }

        .submit-btn {
            background: var(--primary);
            color: var(--white);
            padding: 1rem 2.5rem;
            border: none;
            border-radius: 50px;
            font-family: 'Poppins', sans-serif;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }

        .submit-btn:hover {
            background: var(--primary-light);
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(8, 145, 178, 0.3);
        }

        /* Contact Info Bar */
        .contact-info-bar {
            background: var(--white);
            padding: 40px 5%;
            border-top: 1px solid #e2e8f0;
        }

        .info-row {
            max-width: 800px;
            margin: 0 auto;
            display: flex;
            justify-content: center;
            gap: 3rem;
            flex-wrap: wrap;
        }

        .info-item {
            text-align: center;
        }

        .info-item span {
            font-size: 1.2rem;
            display: block;
            margin-bottom: 0.3rem;
        }

        .info-item p {
            color: var(--gray);
            font-size: 0.85rem;
        }

        .info-item a {
            color: var(--gray);
            text-decoration: none;
            transition: color 0.3s ease;
        }

        .info-item a:hover {
            color: var(--primary);
        }

        /* Footer */
        footer {
            background: var(--darker);
            padding: 40px 5%;
            text-align: center;
        }

        .footer-bottom {
            color: var(--gray-light);
            font-size: 0.9rem;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }

            .contact-hero h1 {
                font-size: 2.2rem;
            }

            .info-row {
                gap: 2rem;
            }
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav>
        <a href="/" class="logo">
            <img src="/static/logo.svg" alt="NexYouth Logo">
        </a>
        <ul class="nav-links">
            <li><a href="/">Home</a></li>
            <li><a href="/#about">About</a></li>
            <li><a href="/#programs">Programs</a></li>
            <li><a href="/#events">Events</a></li>
            <li><a href="/contact">Contact</a></li>
            <li><a href="mailto:nexyouth.master@gmail.com" class="nav-btn">Get Involved →</a></li>
        </ul>
    </nav>

    <!-- Hero -->
    <section class="contact-hero">
        <span>Contact</span>
        <h1>Get In Touch</h1>
    </section>

    <!-- Main Content -->
    <section class="contact-main">
        <div class="contact-form">
            <h2>Send us a message</h2>
            <form action="mailto:nexyouth.master@gmail.com" method="post" enctype="text/plain">
                <div class="form-group">
                    <input type="text" name="name" placeholder="Your Name" required>
                </div>
                <div class="form-group">
                    <input type="email" name="email" placeholder="Your Email" required>
                </div>
                <div class="form-group">
                    <textarea name="message" placeholder="Your Message" required></textarea>
                </div>
                <button type="submit" class="submit-btn">Send Message →</button>
            </form>
        </div>
    </section>

    <!-- Contact Info Bar -->
    <section class="contact-info-bar">
        <div class="info-row">
            <div class="info-item">
                <span>📍</span>
                <p>Toronto, Canada</p>
            </div>
            <div class="info-item">
                <span>✉️</span>
                <p><a href="mailto:nexyouth.master@gmail.com">nexyouth.master@gmail.com</a></p>
            </div>
            <div class="info-item">
                <span>📷</span>
                <p><a href="https://www.instagram.com/nexyouth.ngo/" target="_blank">Instagram</a></p>
            </div>
            <div class="info-item">
                <span>💼</span>
                <p><a href="https://www.linkedin.com/company/nexyouth-society/" target="_blank">LinkedIn</a></p>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="footer-bottom">
            <p>&copy; 2024 NexYouth. All Rights Reserved.</p>
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
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #0891b2;
            --primary-light: #22d3ee;
            --dark: #1e293b;
            --darker: #0f172a;
            --light: #f8fafc;
            --white: #ffffff;
            --gray: #64748b;
            --gray-light: #94a3b8;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background: var(--light);
            color: var(--dark);
            line-height: 1.6;
        }

        /* Navigation */
        nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            padding: 1rem 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        .logo img {
            height: 45px;
        }

        .nav-links {
            display: flex;
            gap: 2.5rem;
            list-style: none;
            align-items: center;
        }

        .nav-links a {
            color: var(--dark);
            text-decoration: none;
            font-weight: 500;
            font-size: 0.95rem;
            transition: color 0.3s ease;
        }

        .nav-links a:hover {
            color: var(--primary);
        }

        .nav-btn {
            background: var(--primary);
            color: var(--white);
            padding: 0.7rem 1.8rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .nav-btn:hover {
            background: var(--primary-light);
            transform: translateY(-2px);
        }

        /* Hero */
        .about-hero {
            padding: 140px 5% 60px;
            text-align: center;
            background: var(--white);
        }

        .about-hero span {
            color: var(--primary);
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 3px;
            font-weight: 600;
        }

        .about-hero h1 {
            font-size: 3rem;
            font-weight: 700;
            color: var(--dark);
            margin-top: 0.5rem;
        }

        /* Who We Are Section */
        .who-we-are {
            padding: 80px 5%;
            background: var(--white);
        }

        .who-content {
            max-width: 1100px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 60px;
            align-items: center;
        }

        .who-text h2 {
            font-size: 2.2rem;
            color: var(--dark);
            margin-bottom: 1.5rem;
        }

        .who-text p {
            color: var(--gray);
            font-size: 1rem;
            line-height: 1.8;
            margin-bottom: 1rem;
        }

        .who-image {
            text-align: center;
        }

        .who-image img {
            width: 100%;
            max-width: 400px;
            border-radius: 20px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.1);
        }

        .founder-card {
            background: var(--light);
            border-radius: 20px;
            padding: 2rem;
            text-align: center;
        }

        .founder-card .avatar {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
            margin: 0 auto 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3rem;
            color: white;
        }

        .founder-card h3 {
            font-size: 1.3rem;
            color: var(--dark);
            margin-bottom: 0.3rem;
        }

        .founder-card .role {
            color: var(--primary);
            font-size: 0.9rem;
            font-weight: 500;
            margin-bottom: 1rem;
        }

        .founder-card p {
            color: var(--gray);
            font-size: 0.9rem;
            line-height: 1.7;
        }

        /* Our Story */
        .our-story {
            padding: 80px 5%;
            background: var(--light);
        }

        .story-content {
            max-width: 800px;
            margin: 0 auto;
            text-align: center;
        }

        .story-content h2 {
            font-size: 2rem;
            color: var(--dark);
            margin-bottom: 1.5rem;
        }

        .story-content p {
            color: var(--gray);
            font-size: 1.05rem;
            line-height: 1.9;
            margin-bottom: 1rem;
        }

        /* What We Do */
        .what-we-do {
            padding: 80px 5%;
            background: var(--white);
        }

        .wwd-content {
            max-width: 1000px;
            margin: 0 auto;
        }

        .wwd-content h2 {
            font-size: 2rem;
            color: var(--dark);
            margin-bottom: 1.5rem;
            text-align: center;
        }

        .wwd-content > p {
            color: var(--gray);
            font-size: 1rem;
            line-height: 1.8;
            text-align: center;
            max-width: 700px;
            margin: 0 auto 3rem;
        }

        .wwd-cards {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
        }

        .wwd-card {
            background: var(--light);
            border-radius: 16px;
            padding: 2rem;
            text-align: center;
            transition: all 0.3s ease;
        }

        .wwd-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.1);
        }

        .wwd-card .icon {
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
            border-radius: 12px;
            margin: 0 auto 1.2rem;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
        }

        .wwd-card h3 {
            font-size: 1.1rem;
            color: var(--dark);
            margin-bottom: 0.8rem;
        }

        .wwd-card p {
            color: var(--gray);
            font-size: 0.9rem;
            line-height: 1.6;
        }

        /* Team Section */
        .team {
            padding: 80px 5%;
            background: var(--light);
        }

        .team-content {
            max-width: 1100px;
            margin: 0 auto;
        }

        .team h2 {
            font-size: 2rem;
            color: var(--dark);
            text-align: center;
            margin-bottom: 1rem;
        }

        .team > p {
            color: var(--gray);
            text-align: center;
            max-width: 600px;
            margin: 0 auto 3rem;
        }

        .team-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2rem;
        }

        .team-member {
            background: var(--white);
            border-radius: 16px;
            padding: 1.5rem;
            text-align: center;
            transition: all 0.3s ease;
        }

        .team-member:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.08);
        }

        .team-member .avatar {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
            margin: 0 auto 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            color: white;
        }

        .team-member h4 {
            font-size: 1rem;
            color: var(--dark);
            margin-bottom: 0.2rem;
        }

        .team-member .position {
            color: var(--primary);
            font-size: 0.8rem;
            font-weight: 500;
        }

        /* CTA */
        .cta-section {
            padding: 60px 5%;
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
            text-align: center;
        }

        .cta-section h3 {
            font-size: 1.8rem;
            color: var(--white);
            margin-bottom: 1rem;
        }

        .cta-section p {
            color: rgba(255,255,255,0.9);
            margin-bottom: 1.5rem;
        }

        .cta-section .btn {
            background: var(--white);
            color: var(--primary);
            padding: 1rem 2.5rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            display: inline-block;
            transition: all 0.3s ease;
        }

        .cta-section .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }

        /* Footer */
        footer {
            background: var(--darker);
            padding: 40px 5%;
            text-align: center;
        }

        .footer-bottom {
            color: var(--gray-light);
            font-size: 0.9rem;
        }

        /* Responsive */
        @media (max-width: 900px) {
            .who-content {
                grid-template-columns: 1fr;
                gap: 40px;
            }

            .wwd-cards {
                grid-template-columns: 1fr;
            }

            .team-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }

            .about-hero h1 {
                font-size: 2.2rem;
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
        <a href="/" class="logo">
            <img src="/static/logo.svg" alt="NexYouth Logo">
        </a>
        <ul class="nav-links">
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/#programs">Programs</a></li>
            <li><a href="/#events">Events</a></li>
            <li><a href="/contact">Contact</a></li>
            <li><a href="mailto:nexyouth.master@gmail.com" class="nav-btn">Get Involved →</a></li>
        </ul>
    </nav>

    <!-- Hero -->
    <section class="about-hero">
        <span>About Us</span>
        <h1>Who We Are</h1>
    </section>

    <!-- Who We Are -->
    <section class="who-we-are">
        <div class="who-content">
            <div class="who-text">
                <h2>Our Community of Changemakers</h2>
                <p>At the heart of NexYouth is our inspiring community of volunteers — passionate individuals who dedicate their time, skills, and creativity to driving meaningful change.</p>
                <p>Coming from diverse backgrounds in science, education, advocacy, and the arts, our volunteers share a common commitment to protecting the environment and empowering youth.</p>
                <p>Get to know the dedicated changemakers who make our mission possible!</p>
            </div>
            <div class="who-image" style="display: flex; gap: 1.5rem; flex-wrap: wrap; justify-content: center;">
                <div class="founder-card" style="flex: 1; min-width: 200px; max-width: 250px;">
                    <img src="https://www.nexyouth.org/Member_Jhuan1.jpg" alt="Justin Huang" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
                    <h3>Justin Huang</h3>
                    <p class="role">Co-Founder</p>
                    <p>Justin is an enthusiast of the environment and an avid reader. He hopes that through NexYouth, others will find their own passion for global issues.</p>
                </div>
                <div class="founder-card" style="flex: 1; min-width: 200px; max-width: 250px;">
                    <img src="https://www.nexyouth.org/Member_Mwen1.jpg" alt="Max Wen" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; object-position: center top; margin-bottom: 1rem;">
                    <h3>Max Wen</h3>
                    <p class="role">Co-Founder</p>
                    <p>Max has been debating and teaching for over 2 years. He enjoys public speaking, STEM, and content creation.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Our Story Section -->
    <section class="our-story">
        <div class="story-content">
            <h2>Our Story</h2>
            <p>NexYouth was founded by passionate high school students who believe in the power of youth to create meaningful change. Together, they've built a platform that connects young people with opportunities for growth and impact.</p>
        </div>
    </section>

    <!-- What We Do -->
    <section class="what-we-do">
        <div class="wwd-content">
            <h2>What We Do</h2>
            <p>At NexYouth, we create pathways for young people to develop skills, gain experience, and connect with mentors who can guide their journey.</p>
            
            <div class="wwd-cards">
                <div class="wwd-card">
                    <div class="icon">🎯</div>
                    <h3>Debate Coaching</h3>
                    <p>Learn from competitive debaters who have won at national and international tournaments.</p>
                </div>
                <div class="wwd-card">
                    <div class="icon">📚</div>
                    <h3>Academic Tutoring</h3>
                    <p>Science, economics, and STEM instruction from gifted high school scholars.</p>
                </div>
                <div class="wwd-card">
                    <div class="icon">✍️</div>
                    <h3>Writing Contests</h3>
                    <p>Creative writing competitions organized by passionate young writers and sci-fi enthusiasts.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Team -->
    <section class="team">
        <div class="team-content">
            <h2>Our Team</h2>
            <p>Meet the passionate youth leaders who make NexYouth possible.</p>
            
            <div class="team-grid">
                <div class="team-member">
                    <img src="https://www.nexyouth.org/Member_Jhuan1.jpg" alt="Justin Huang" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
                    <h4>Justin Huang</h4>
                    <p class="position">Co-Founder</p>
                </div>
                <div class="team-member">
                    <img src="https://www.nexyouth.org/Member_Mwen1.jpg" alt="Max Wen" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; object-position: center top; margin-bottom: 1rem;">
                    <h4>Max Wen</h4>
                    <p class="position">Co-Founder</p>
                </div>
                <div class="team-member">
                    <img src="https://www.nexyouth.org/Member_Suzea1.png" alt="Stephanie Uzea" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
                    <h4>Stephanie Uzea</h4>
                    <p class="position">Canada President & Director of Operations</p>
                </div>
                <div class="team-member">
                    <img src="https://www.nexyouth.org/Member_Eluo1.png" alt="Ethan Luo" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
                    <h4>Ethan Luo</h4>
                    <p class="position">Oakville Chapter President</p>
                </div>
                <div class="team-member">
                    <img src="https://www.nexyouth.org/Member_Rwei1.png" alt="Rachel Wei" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
                    <h4>Rachel Wei</h4>
                    <p class="position">Coquitlam Chapter President</p>
                </div>
                <div class="team-member">
                    <img src="https://www.nexyouth.org/Member_Xyang1.jpg" alt="Xuhan Yang" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
                    <h4>Xuhan Yang</h4>
                    <p class="position">Director of Technology</p>
                </div>
                <div class="team-member">
                    <img src="https://www.nexyouth.org/Member_Chuan1.jpg" alt="Chloe Huang" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
                    <h4>Chloe Huang</h4>
                    <p class="position">Secretary</p>
                </div>
                <div class="team-member">
                    <img src="https://www.nexyouth.org/Member_Kjosh1.png" alt="Keerti Joshi" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
                    <h4>Keerti Joshi</h4>
                    <p class="position">Debate Coach</p>
                </div>
                <div class="team-member">
                    <img src="https://www.nexyouth.org/Member_Kyip1.png" alt="Kristen Yip" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
                    <h4>Kristen Yip</h4>
                    <p class="position">Debate Coach</p>
                </div>
                <div class="team-member">
                    <img src="https://www.nexyouth.org/Member_Czhan1.png" alt="Cody Zhang" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
                    <h4>Cody Zhang</h4>
                    <p class="position">Economics Instructor</p>
                </div>
                <div class="team-member">
                    <img src="https://www.nexyouth.org/Member_Jliu1.png" alt="Jeffrey Liu" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
                    <h4>Jeffrey Liu</h4>
                    <p class="position">Debate Coach</p>
                </div>
                <div class="team-member">
                    <img src="https://www.nexyouth.org/Member_Aliu1.png" alt="Amy Liu" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
                    <h4>Amy Liu</h4>
                    <p class="position">Debate Coach</p>
                </div>
                <div class="team-member">
                    <img src="https://www.nexyouth.org/Member_Fzhan1.jpg" alt="Ferrari Zhang" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
                    <h4>Ferrari Zhang</h4>
                    <p class="position">Debate Coach</p>
                </div>
                <div class="team-member">
                    <img src="https://www.nexyouth.org/Member_Tguo1.png" alt="Terrence Guo" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
                    <h4>Terrence Guo</h4>
                    <p class="position">Debate Coach</p>
                </div>
                <div class="team-member">
                    <img src="https://www.nexyouth.org/Member_Yshua1.png" alt="Yunfei Shuai" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
                    <h4>Yunfei Shuai</h4>
                    <p class="position">Contests Organizer</p>
                </div>
                <div class="team-member">
                    <img src="https://www.nexyouth.org/Member_Szhen1.png" alt="Susan Zheng" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
                    <h4>Susan Zheng</h4>
                    <p class="position">Contests Organizer</p>
                </div>
                <div class="team-member">
                    <img src="https://www.nexyouth.org/Member_Sisla1.png" alt="Shahrad Islam" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
                    <h4>Shahrad Islam</h4>
                    <p class="position">Science Instructor</p>
                </div>
                <div class="team-member">
                    <img src="https://www.nexyouth.org/Member_Rliu1.png" alt="Ronnie Liu" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem;">
                    <h4>Ronnie Liu</h4>
                    <p class="position">Science Instructor</p>
                </div>
                <div class="team-member">
                    <div class="avatar">👥</div>
                    <h4>Rest of the Team</h4>
                    <p class="position">Instructors & Volunteers</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="cta-section">
        <h3>Join Our Community</h3>
        <p>Ready to make a difference? Become part of our passionate team of changemakers.</p>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLSc-FbV-GMP_rSv8mAYaFT-QxQzdWJqYcRXd_7QfwITUNkQzhw/viewform" class="btn" target="_blank">Get Involved →</a>
    </section>

    <!-- Footer -->
    <footer>
        <div class="footer-bottom">
            <p>&copy; 2024 NexYouth. All Rights Reserved.</p>
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
            <p>&copy; 2023 NexYouth. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/about')
def about():
    return render_template_string(ABOUT_TEMPLATE)

@app.route('/contact')
def contact():
    return render_template_string(CONTACT_TEMPLATE)

@app.route('/partner')
def partner():
    return render_template_string(PARTNER_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
