from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__, static_folder='static', static_url_path='/static', template_folder='templates')

@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serve static files from static folder"""
    return send_from_directory(os.path.join(os.path.dirname(__file__), 'static'), filename)

# ============== ROUTES ==============

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

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

@app.route('/programs/youth-tech-lab')
def youth_tech_lab():
    return render_template('youth-tech-lab.html')

# Partner Routes
@app.route('/partner')
def partner():
    return render_template('partner.html')

@app.route('/partnership-packages')
def partnership_packages():
    return render_template('partnership-packages.html')

# Contact Route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Success Page
@app.route('/success')
def success():
    return render_template('success.html')

# Catch-all route for client-side routing
@app.route('/<path:path>')
def catch_all(path):
    """Catch all routes and return the main page for client-side routing"""
    if path == 'about':
        return render_template('about.html')
    if path == 'contact':
        return render_template('contact.html')
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
