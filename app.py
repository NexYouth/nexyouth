from flask import Flask, render_template, send_from_directory, request, jsonify, Response, send_file
import os
import csv
import re
from datetime import datetime, timezone
from functools import wraps

app = Flask(__name__, static_folder='static', static_url_path='/static', template_folder='templates')

# ============== ECO CLASSROOM REGISTRATION ==============

ECO_REG_FIELDS = [
    'submitted_at', 'student_name', 'age', 'grade', 'school',
    'city', 'country', 'student_email',
    'parent_name', 'parent_email', 'parent_phone',
    'source', 'motivation', 'consent', 'ip',
]
ECO_REG_FILE = os.path.join(os.path.dirname(__file__), 'data', 'eco-registrations.csv')

def _ensure_eco_csv():
    os.makedirs(os.path.dirname(ECO_REG_FILE), exist_ok=True)
    if not os.path.exists(ECO_REG_FILE):
        with open(ECO_REG_FILE, 'w', newline='', encoding='utf-8') as f:
            csv.DictWriter(f, fieldnames=ECO_REG_FIELDS).writeheader()

@app.route('/api/eco-classroom/register', methods=['POST'])
def eco_classroom_register():
    data = request.get_json(silent=True) or {}
    required = ['student_name', 'city', 'country', 'student_email',
                'parent_name', 'parent_email', 'consent']
    missing = [k for k in required if not str(data.get(k, '')).strip()]
    if missing:
        return jsonify({'ok': False, 'error': f"Missing required fields: {', '.join(missing)}"}), 400

    email = str(data.get('student_email', '')).strip()
    if not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email):
        return jsonify({'ok': False, 'error': 'Please enter a valid student email.'}), 400
    parent_email = str(data.get('parent_email', '')).strip()
    if not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', parent_email):
        return jsonify({'ok': False, 'error': 'Please enter a valid parent/guardian email.'}), 400

    row = {k: str(data.get(k, '')).strip()[:500] for k in ECO_REG_FIELDS}
    row['submitted_at'] = datetime.now(timezone.utc).isoformat(timespec='seconds')
    row['ip'] = (request.headers.get('X-Forwarded-For') or request.remote_addr or '').split(',')[0].strip()

    try:
        _ensure_eco_csv()
        with open(ECO_REG_FILE, 'a', newline='', encoding='utf-8') as f:
            csv.DictWriter(f, fieldnames=ECO_REG_FIELDS).writerow(row)
    except OSError as e:
        return jsonify({'ok': False, 'error': 'Unable to save registration. Please email NexYouth directly.'}), 500

    return jsonify({'ok': True})


# ============== ECO CLASSROOM SUBMISSIONS / AUTO-GRADING / COMPLETION ==============

QUIZ_ANSWERS = {
    'quiz1': ['A','B','B','A','B','D','D','D','A','D'],
    'quiz2': ['A','A','A','B','D','C','A','D','D','D'],
}
QUIZ_PASS = 6
TASK_MIN_CHARS = 30
FINAL_MIN_WORDS = 100

ECO_SUB_FILE = os.path.join(os.path.dirname(__file__), 'data', 'eco-submissions.csv')
ECO_SUB_FIELDS = ['submitted_at','student_email','type','lesson_id','content','score','max_score','passed','ip']
ECO_DONE_FILE = os.path.join(os.path.dirname(__file__), 'data', 'eco-completed.csv')
ECO_EMAIL_LOG = os.path.join(os.path.dirname(__file__), 'data', 'sent-emails.log')

def _ensure_sub_csv():
    os.makedirs(os.path.dirname(ECO_SUB_FILE), exist_ok=True)
    if not os.path.exists(ECO_SUB_FILE):
        with open(ECO_SUB_FILE, 'w', newline='', encoding='utf-8') as f:
            csv.DictWriter(f, fieldnames=ECO_SUB_FIELDS).writeheader()

def _ensure_done_csv():
    os.makedirs(os.path.dirname(ECO_DONE_FILE), exist_ok=True)
    if not os.path.exists(ECO_DONE_FILE):
        with open(ECO_DONE_FILE, 'w', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow(['completed_at','student_email','student_name'])

def _read_progress(email):
    email = email.lower().strip()
    tasks, q1, q2, fw = set(), None, None, 0
    if os.path.exists(ECO_SUB_FILE):
        with open(ECO_SUB_FILE, 'r', encoding='utf-8') as f:
            for r in csv.DictReader(f):
                if (r.get('student_email') or '').lower().strip() != email:
                    continue
                t, lid = r.get('type'), r.get('lesson_id')
                if t == 'task' and lid:
                    tasks.add(lid)
                elif t == 'quiz1':
                    try: q1 = max(q1 or 0, int(r.get('score') or 0))
                    except ValueError: pass
                elif t == 'quiz2':
                    try: q2 = max(q2 or 0, int(r.get('score') or 0))
                    except ValueError: pass
                elif t == 'final':
                    try: fw = max(fw, int(r.get('score') or 0))
                    except ValueError: pass
    return {'tasks_done': sorted(tasks, key=lambda x: int(x) if x.isdigit() else 99), 'quiz1': q1, 'quiz2': q2, 'final_words': fw}

def _is_completed(p):
    return (len(p['tasks_done']) >= 9
            and (p['quiz1'] or 0) >= QUIZ_PASS
            and (p['quiz2'] or 0) >= QUIZ_PASS
            and p['final_words'] >= FINAL_MIN_WORDS)

def _already_emailed(email):
    if not os.path.exists(ECO_DONE_FILE):
        return False
    email = email.lower().strip()
    with open(ECO_DONE_FILE, 'r', encoding='utf-8') as f:
        next(f, None)
        for line in f:
            parts = [p.strip() for p in line.split(',', 2)]
            if len(parts) >= 2 and parts[1].lower() == email:
                return True
    return False

def _student_name(email):
    if not os.path.exists(ECO_REG_FILE):
        return ''
    email = email.lower().strip()
    with open(ECO_REG_FILE, 'r', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            if (r.get('student_email') or '').lower().strip() == email:
                return r.get('student_name', '')
    return ''

def _completion_info(email):
    """Return {'completed_at': iso, 'name': str} if student has completed, else None."""
    if not os.path.exists(ECO_DONE_FILE):
        return None
    email = email.lower().strip()
    with open(ECO_DONE_FILE, 'r', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            if (r.get('student_email') or '').lower().strip() == email:
                return {
                    'completed_at': r.get('completed_at', ''),
                    'name': r.get('student_name', '') or _student_name(email),
                }
    return None

ADMIN_CC_EMAIL = 'nexyouth.master@gmail.com'

def _generate_certificate(name, completion_date=None):
    """Generate a NexYouth EcoHero certificate PDF and return (bytes, cert_id)."""
    try:
        from reportlab.lib.pagesizes import landscape, letter
        from reportlab.pdfgen import canvas
        from reportlab.lib.colors import HexColor
        from reportlab.lib.units import inch
    except ImportError:
        return None, None

    import io
    import hashlib

    if not completion_date:
        completion_date = datetime.now(timezone.utc).strftime('%B %d, %Y')
    if not name:
        name = "Student"

    sid = hashlib.md5(f"{name}|{completion_date}|{datetime.now(timezone.utc).isoformat()}".encode()).hexdigest()[:8].upper()
    cert_id = f"NY-ECO-{datetime.now(timezone.utc).strftime('%Y')}-{sid}"

    buf = io.BytesIO()
    page_size = landscape(letter)
    c = canvas.Canvas(buf, pagesize=page_size)
    W, H = page_size

    GREEN = HexColor('#1A6640')
    LEAF = HexColor('#3FB572')
    GOLD = HexColor('#C9A84C')
    DARK = HexColor('#18182A')
    CREAM = HexColor('#F8F5F0')

    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    margin = 0.5 * inch
    c.setStrokeColor(GREEN); c.setLineWidth(6)
    c.rect(margin, margin, W - 2 * margin, H - 2 * margin, fill=0, stroke=1)
    inner = margin + 10
    c.setStrokeColor(GOLD); c.setLineWidth(1)
    c.rect(inner, inner, W - 2 * inner, H - 2 * inner, fill=0, stroke=1)

    c.setFillColor(GREEN); c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(W / 2, H - 1.0 * inch, "N E X Y O U T H")
    c.setFillColor(GOLD); c.setFont("Helvetica-Oblique", 10)
    c.drawCentredString(W / 2, H - 1.25 * inch, "- CREATING SPACE FOR YOUTH -")

    c.setStrokeColor(GOLD); c.setLineWidth(1)
    c.line(W / 2 - 2 * inch, H - 1.45 * inch, W / 2 + 2 * inch, H - 1.45 * inch)

    c.setFillColor(DARK); c.setFont("Times-Bold", 38)
    c.drawCentredString(W / 2, H - 2.1 * inch, "Certificate of Completion")

    c.setFillColor(LEAF); c.setFont("Times-BoldItalic", 24)
    c.drawCentredString(W / 2, H - 2.6 * inch, "EcoHero")

    c.setFillColor(DARK); c.setFont("Times-Roman", 14)
    c.drawCentredString(W / 2, H - 3.2 * inch, "This certificate is proudly presented to")

    c.setFillColor(GREEN); c.setFont("Times-Bold", 32)
    c.drawCentredString(W / 2, H - 3.95 * inch, name)

    name_width = c.stringWidth(name, "Times-Bold", 32)
    c.setStrokeColor(GOLD); c.setLineWidth(1.5)
    c.line(W / 2 - name_width / 2 - 20, H - 4.1 * inch,
           W / 2 + name_width / 2 + 20, H - 4.1 * inch)

    c.setFillColor(DARK); c.setFont("Times-Roman", 13)
    c.drawCentredString(W / 2, H - 4.55 * inch,
                        "for successfully completing the NexYouth Eco Literacy Course:")
    c.setFillColor(GREEN); c.setFont("Times-BoldItalic", 16)
    c.drawCentredString(W / 2, H - 4.95 * inch,
                        "Eco Literacy: From Environmental Systems to Youth Action")

    c.setFillColor(DARK); c.setFont("Times-Italic", 11)
    c.drawCentredString(W / 2, H - 5.4 * inch,
                        "9 Lessons   |   2 Quizzes Passed (60%+)   |   Youth Eco Action Plan Submitted")

    sig_y = 1.4 * inch

    # LEFT — Director signature (italic name above line, label below)
    c.setFillColor(DARK); c.setFont("Times-Italic", 16)
    c.drawCentredString(2.5 * inch, sig_y + 6, "Justin Huang & Max Wen")
    c.setStrokeColor(DARK); c.setLineWidth(0.5)
    c.line(1.5 * inch, sig_y, 3.5 * inch, sig_y)
    c.setFont("Helvetica", 10)
    c.drawCentredString(2.5 * inch, sig_y - 15, "NexYouth Program Director")

    # RIGHT — Date (italic date above line, label below)
    c.setFont("Times-Italic", 16)
    c.drawCentredString(W - 2.5 * inch, sig_y + 6, completion_date)
    c.line(W - 3.5 * inch, sig_y, W - 1.5 * inch, sig_y)
    c.setFont("Helvetica", 10)
    c.drawCentredString(W - 2.5 * inch, sig_y - 15, "Date Issued")

    # Bottom strip (between the two borders) — cert id + brand
    c.setFont("Helvetica", 8); c.setFillColor(DARK)
    c.drawRightString(W - margin - 10, margin + 8, f"Certificate ID: {cert_id}")
    c.drawString(margin + 10, margin + 8, "nexyouth.org")

    c.save()
    buf.seek(0)
    return buf.getvalue(), cert_id


def _send_completion_email(email, name):
    full_name = (name or '').strip() or 'Student'
    first_name = full_name.split()[0] if full_name != 'Student' else 'there'

    cert_pdf, cert_id = _generate_certificate(full_name)

    # Save certificate to disk for archive / admin reference
    cert_path = None
    if cert_pdf:
        cert_dir = os.path.join(os.path.dirname(__file__), 'data', 'certificates')
        os.makedirs(cert_dir, exist_ok=True)
        safe_email = re.sub(r'[^A-Za-z0-9._-]', '_', email)
        cert_path = os.path.join(cert_dir, f"{safe_email}-{cert_id}.pdf")
        with open(cert_path, 'wb') as f:
            f.write(cert_pdf)

    subject = f"NexYouth EcoHero Certificate - {full_name} (Course Complete)"

    text_body = (
        f"Hi {first_name},\n\n"
        "Congratulations on completing the NexYouth Eco Literacy course!\n\n"
        "You have successfully:\n"
        "  - Completed all 9 lessons\n"
        "  - Passed both course quizzes with 60% or higher\n"
        "  - Submitted your Youth Eco Action Plan\n\n"
        "Attached to this email is your NexYouth EcoHero Certificate (PDF).\n"
        "You have also earned a $15 completion award.\n\n"
        "ACTION REQUIRED: e-Transfer Email\n\n"
        "We will send your $15 award by Interac e-Transfer.\n\n"
        f"The email we have on file for you is:\n   {email}\n\n"
        "Please REPLY to this email to confirm:\n"
        "  1) That this address can receive Interac e-Transfers, OR\n"
        "  2) The correct e-Transfer email you would like us to use.\n\n"
        "We will process your payment within 3-5 business days of receiving\n"
        "your confirmation.\n\n"
        "Thank you for taking real action on the environment.\n\n"
        "- The NexYouth Team\n"
    )

    html_body = (
        '<!DOCTYPE html><html><body style="font-family:Arial,Helvetica,sans-serif;'
        'font-size:14px;color:#202124;max-width:640px;margin:0 auto;padding:18px;line-height:1.55">'
        f'<p>Hi <strong>{first_name}</strong>,</p>'
        '<p>Congratulations on completing the <strong>NexYouth Eco Literacy course</strong>!</p>'
        '<p>You have successfully:</p>'
        '<ul style="padding-left:22px;margin:8px 0">'
        '<li>Completed all 9 lessons</li>'
        '<li>Passed both course quizzes with 60% or higher</li>'
        '<li>Submitted your Youth Eco Action Plan</li>'
        '</ul>'
        '<p>Attached to this email is your <strong>NexYouth EcoHero Certificate</strong> (PDF).<br>'
        'You have also earned a <strong>$15 completion award</strong>.</p>'
        '<p style="margin-top:22px;font-size:16px"><strong style="color:#1A73E8">'
        'ACTION REQUIRED: e-Transfer Email</strong></p>'
        '<p>We will send your $15 award by Interac e-Transfer.</p>'
        '<p>The email we have on file for you is:<br>'
        f'&nbsp;&nbsp;&nbsp;<a href="mailto:{email}" style="color:#1A73E8">{email}</a></p>'
        '<p>Please <strong>REPLY</strong> to this email to confirm:</p>'
        '<ol style="padding-left:22px;margin:8px 0">'
        '<li>That this address can receive Interac e-Transfers, OR</li>'
        '<li>The correct e-Transfer email you would like us to use.</li>'
        '</ol>'
        '<p>We will process your payment within 3-5 business days of receiving your confirmation.</p>'
        '<p style="margin-top:22px">Thank you for taking real action on the environment.</p>'
        '<p style="color:#5F6368;margin-top:18px">— The NexYouth Team</p>'
        '</body></html>'
    )

    # Always log (plain text for readability)
    os.makedirs(os.path.dirname(ECO_EMAIL_LOG), exist_ok=True)
    with open(ECO_EMAIL_LOG, 'a', encoding='utf-8') as f:
        f.write(f"\n--- {datetime.now(timezone.utc).isoformat(timespec='seconds')} ---\n")
        f.write(f"To: {email}\nCc: {ADMIN_CC_EMAIL}\nSubject: {subject}\n")
        if cert_path:
            f.write(f"Attachment: {os.path.basename(cert_path)} ({len(cert_pdf)} bytes)\n")
        f.write(f"\n{text_body}\n")

    smtp_host = os.environ.get('SMTP_HOST')
    if not smtp_host:
        return 'logged'

    import smtplib, traceback
    from email.message import EmailMessage as _EmailMessage
    try:
        msg = _EmailMessage()
        msg['Subject'] = subject
        msg['From'] = os.environ.get('EMAIL_FROM', 'noreply@nexyouth.org')
        msg['To'] = email
        msg['Cc'] = ADMIN_CC_EMAIL
        msg.set_content(text_body)
        msg.add_alternative(html_body, subtype='html')
        if cert_pdf:
            msg.add_attachment(cert_pdf, maintype='application', subtype='pdf',
                               filename=f'NexYouth-EcoHero-{cert_id}.pdf')
        port = int(os.environ.get('SMTP_PORT', '587'))
        use_ssl = os.environ.get('SMTP_SSL', '').lower() in ('1', 'true', 'yes') or port == 465
        recipients = [email, ADMIN_CC_EMAIL]
        timeout = int(os.environ.get('SMTP_TIMEOUT', '30'))

        if use_ssl:
            smtp_cls = smtplib.SMTP_SSL
            kwargs = {'timeout': timeout}
        else:
            smtp_cls = smtplib.SMTP
            kwargs = {'timeout': timeout}

        with smtp_cls(smtp_host, port, **kwargs) as s:
            if not use_ssl and os.environ.get('SMTP_TLS', '1') == '1':
                s.starttls()
            u, p = os.environ.get('SMTP_USER'), os.environ.get('SMTP_PASS')
            if u and p:
                s.login(u, p)
            s.send_message(msg, to_addrs=recipients)
        with open(ECO_EMAIL_LOG, 'a', encoding='utf-8') as f:
            f.write(f"SMTP delivery: SUCCESS to {email} cc {ADMIN_CC_EMAIL} via {smtp_host}:{port} (ssl={use_ssl})\n")
        return 'sent'
    except Exception as e:
        with open(ECO_EMAIL_LOG, 'a', encoding='utf-8') as f:
            f.write(f"SMTP error ({type(e).__name__}): {e}\n")
            f.write(traceback.format_exc())
        return 'error'

@app.route('/api/eco-classroom/submit', methods=['POST'])
def eco_classroom_submit():
    data = request.get_json(silent=True) or {}
    email = str(data.get('student_email') or '').strip().lower()
    sub_type = str(data.get('type') or '').strip()

    if not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email):
        return jsonify({'ok': False, 'error': 'Please register first or enter a valid email.'}), 400
    if sub_type not in ('task', 'quiz1', 'quiz2', 'final'):
        return jsonify({'ok': False, 'error': 'Invalid submission type.'}), 400

    score = max_score = ''
    passed = '0'
    content = ''
    lesson_id = ''

    if sub_type == 'task':
        lesson_id = str(data.get('lesson_id') or '').strip()
        if lesson_id not in [str(i) for i in range(1, 10)]:
            return jsonify({'ok': False, 'error': 'Invalid lesson id.'}), 400
        content = ''  # no response required — lessons are marked complete by the student
        passed = '1'

    elif sub_type in ('quiz1', 'quiz2'):
        answers = data.get('answers')
        if not isinstance(answers, list) or len(answers) != 10:
            return jsonify({'ok': False, 'error': 'Please answer all 10 questions.'}), 400
        key = QUIZ_ANSWERS[sub_type]
        s = sum(1 for i, a in enumerate(answers) if str(a).strip().upper() == key[i])
        score, max_score = str(s), '10'
        passed = '1' if s >= QUIZ_PASS else '0'
        content = ','.join(str(a).strip().upper()[:1] for a in answers)
        lesson_id = sub_type

    else:  # final
        content = str(data.get('content') or '').strip()[:8000]
        words = len(re.findall(r"[A-Za-z\u4e00-\u9fff]+", content))
        score, max_score = str(words), str(FINAL_MIN_WORDS)
        if words < FINAL_MIN_WORDS:
            return jsonify({'ok': False, 'error': f'Your action plan is {words} words. Please write at least {FINAL_MIN_WORDS} words.'}), 400
        passed = '1'
        lesson_id = 'final'

    row = {
        'submitted_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'student_email': email,
        'type': sub_type,
        'lesson_id': lesson_id,
        'content': content,
        'score': score,
        'max_score': max_score,
        'passed': passed,
        'ip': (request.headers.get('X-Forwarded-For') or request.remote_addr or '').split(',')[0].strip(),
    }

    try:
        _ensure_sub_csv()
        with open(ECO_SUB_FILE, 'a', newline='', encoding='utf-8') as f:
            csv.DictWriter(f, fieldnames=ECO_SUB_FIELDS).writerow(row)
    except OSError:
        return jsonify({'ok': False, 'error': 'Could not save submission.'}), 500

    progress = _read_progress(email)
    completed_now = False
    email_status = None
    if _is_completed(progress) and not _already_emailed(email):
        name = _student_name(email)
        _ensure_done_csv()
        with open(ECO_DONE_FILE, 'a', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow([
                datetime.now(timezone.utc).isoformat(timespec='seconds'), email, name
            ])
        email_status = _send_completion_email(email, name)
        completed_now = True

    return jsonify({
        'ok': True,
        'score': score,
        'max_score': max_score,
        'passed': passed == '1',
        'progress': progress,
        'completed': _is_completed(progress),
        'completed_now': completed_now,
        'email_status': email_status,
    })

@app.route('/api/eco-classroom/login', methods=['POST'])
def eco_classroom_login():
    data = request.get_json(silent=True) or {}
    email = str(data.get('student_email') or '').strip().lower()
    if not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email):
        return jsonify({'ok': False, 'error': 'Please enter a valid email.'}), 400

    if not os.path.exists(ECO_REG_FILE):
        return jsonify({'ok': False, 'error': 'No registrations found. Please register first.'}), 404

    student = None
    with open(ECO_REG_FILE, 'r', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            if (r.get('student_email') or '').lower().strip() == email:
                student = r
                break

    if not student:
        return jsonify({'ok': False, 'error': 'No registration found for this email. Please register first.'}), 404

    progress = _read_progress(email)
    return jsonify({
        'ok': True,
        'student': {
            'email': email,
            'name': student.get('student_name', ''),
        },
        'progress': progress,
        'completed': _is_completed(progress),
        'completion_info': _completion_info(email),
    })

@app.route('/api/eco-classroom/progress', methods=['GET'])
def eco_classroom_progress():
    email = (request.args.get('email') or '').strip().lower()
    if not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email):
        return jsonify({'ok': False, 'error': 'Valid email required.'}), 400
    progress = _read_progress(email)
    return jsonify({
        'ok': True,
        'progress': progress,
        'completed': _is_completed(progress),
        'completion_info': _completion_info(email),
    })

# ============== ECO CLASSROOM ADMIN ==============

def _check_admin_auth():
    auth = request.authorization
    expected_user = os.environ.get('ADMIN_USER', 'admin')
    expected_pass = os.environ.get('ADMIN_PASSWORD', '')
    if not expected_pass:
        return False
    if not auth:
        return False
    return auth.username == expected_user and auth.password == expected_pass

def _admin_unauthorized():
    msg = 'Admin access requires authentication. Set ADMIN_USER and ADMIN_PASSWORD in .env'
    return Response(msg, 401, {'WWW-Authenticate': 'Basic realm="NexYouth EcoClassroom Admin"'})

def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not _check_admin_auth():
            return _admin_unauthorized()
        return f(*args, **kwargs)
    return wrapper

@app.route('/programs/eco-classroom/admin')
@admin_required
def eco_classroom_admin():
    """Admin dashboard: all registered students + progress + completion."""
    registrations = []
    if os.path.exists(ECO_REG_FILE):
        with open(ECO_REG_FILE, 'r', encoding='utf-8') as f:
            registrations = list(csv.DictReader(f))

    completed = {}
    if os.path.exists(ECO_DONE_FILE):
        with open(ECO_DONE_FILE, 'r', encoding='utf-8') as f:
            for r in csv.DictReader(f):
                e = (r.get('student_email') or '').lower().strip()
                if e:
                    completed[e] = {
                        'completed_at': r.get('completed_at', ''),
                        'name': r.get('student_name', ''),
                    }

    # If a student appears in completed but not in registrations, surface them too
    reg_emails = {(r.get('student_email') or '').lower().strip() for r in registrations}
    for email, info in completed.items():
        if email not in reg_emails:
            registrations.append({
                'submitted_at': '',
                'student_name': info.get('name', '(unknown)'),
                'student_email': email,
                'age': '', 'grade': '', 'school': '',
                'city': '', 'country': '',
                'parent_name': '', 'parent_email': '', 'parent_phone': '',
                'source': '(no registration record)',
                'motivation': '', 'consent': '', 'ip': '',
                '_orphan': True,
            })

    # Annotate with progress + completion
    for reg in registrations:
        email = (reg.get('student_email') or '').lower().strip()
        prog = _read_progress(email) if email else {'tasks_done': [], 'quiz1': None, 'quiz2': None, 'final_words': 0}
        reg['_tasks_done'] = len(prog.get('tasks_done') or [])
        reg['_quiz1'] = prog.get('quiz1')
        reg['_quiz2'] = prog.get('quiz2')
        reg['_final_words'] = prog.get('final_words') or 0
        reg['_milestones'] = (
            reg['_tasks_done']
            + (1 if (reg['_quiz1'] or 0) >= QUIZ_PASS else 0)
            + (1 if (reg['_quiz2'] or 0) >= QUIZ_PASS else 0)
            + (1 if reg['_final_words'] >= FINAL_MIN_WORDS else 0)
        )
        reg['_completed'] = email in completed
        reg['_completed_at'] = completed.get(email, {}).get('completed_at', '')
        # Check if a certificate file exists
        if reg['_completed']:
            cert_dir = os.path.join(os.path.dirname(__file__), 'data', 'certificates')
            if os.path.isdir(cert_dir):
                safe_email = re.sub(r'[^A-Za-z0-9._-]', '_', email)
                certs = [n for n in os.listdir(cert_dir) if n.startswith(safe_email + '-')]
                reg['_cert_file'] = certs[-1] if certs else ''
            else:
                reg['_cert_file'] = ''
        else:
            reg['_cert_file'] = ''

    # Sort: most recent registrations first
    registrations.sort(key=lambda r: r.get('submitted_at') or '', reverse=True)

    stats = {
        'total': len(registrations),
        'completed': sum(1 for r in registrations if r['_completed']),
        'in_progress': sum(1 for r in registrations if not r['_completed'] and r['_milestones'] > 0),
        'not_started': sum(1 for r in registrations if not r['_completed'] and r['_milestones'] == 0),
    }

    return render_template('eco-classroom-admin.html',
                           registrations=registrations,
                           stats=stats,
                           admin_user=request.authorization.username)

@app.route('/programs/eco-classroom/admin/export.csv')
@admin_required
def eco_classroom_admin_export():
    if not os.path.exists(ECO_REG_FILE):
        return ('No registrations yet.', 404)
    return send_file(
        ECO_REG_FILE,
        as_attachment=True,
        download_name=f'eco-registrations-{datetime.now().strftime("%Y%m%d")}.csv',
        mimetype='text/csv',
    )

@app.route('/programs/eco-classroom/admin/cert/<path:filename>')
@admin_required
def eco_classroom_admin_cert(filename):
    cert_dir = os.path.join(os.path.dirname(__file__), 'data', 'certificates')
    # Prevent path traversal
    if '/' in filename or '..' in filename:
        return ('Bad request', 400)
    return send_from_directory(cert_dir, filename, as_attachment=True)


@app.route('/api/eco-classroom/resend-cert', methods=['POST'])
def eco_classroom_resend_cert():
    """Re-generate the certificate and re-send the completion email.
    Bypasses the _already_emailed check so completed students can request
    a fresh certificate at any time."""
    data = request.get_json(silent=True) or {}
    email = str(data.get('student_email') or '').strip().lower()
    if not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email):
        return jsonify({'ok': False, 'error': 'Valid email required.'}), 400

    info = _completion_info(email)
    if not info:
        return jsonify({'ok': False, 'error': 'No completion record found for this email.'}), 404

    name = info.get('name') or _student_name(email)
    status = _send_completion_email(email, name)
    return jsonify({'ok': True, 'email_status': status, 'sent_to': email, 'cc': ADMIN_CC_EMAIL})


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

@app.route('/programs/iyec-2026-results')
def iyec_2026_results():
    return render_template('iyec-2026-results.html')

@app.route('/programs/youth-tech-lab')
def youth_tech_lab():
    return render_template('youth-tech-lab.html')

@app.route('/programs/eco-classroom')
def eco_classroom():
    """Catalog page — lists all available EcoClassroom courses."""
    return render_template('eco-classroom.html')

@app.route('/programs/eco-classroom/eco-literacy')
def eco_classroom_eco_literacy():
    """The Eco Literacy course (formerly the only EcoClassroom page)."""
    return render_template('course-eco-literacy.html')

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
