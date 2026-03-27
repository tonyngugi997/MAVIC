
from flask import Flask, request, jsonify, render_template, render_template
import smtplib
from email.message import EmailMessage
import os
from chatbot import ask_chatbot


# Mailtrap configuratio
MAILTRAP_HOST = "smtp.mailtrap.io"
MAILTRAP_PORT = 587
MAILTRAP_USER = os.getenv('MAILTRAP_USER', 'your_mailtrap_username')
MAILTRAP_PASS = os.getenv('MAILTRAP_PASS', 'your_mailtrap_password')
RECEIVER_EMAIL = "your@mail.com"

app = Flask(__name__, template_folder='/home/Mavicbizz/mysite/templates')
@app.route('/')
def index():
    return render_template('INDEX.html')




@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    response = ask_chatbot(user_message)
    return jsonify({"reply": response})

@app.route("/ping")
def ping():
    return "server is live"


@app.route('/warehousing')
def warehousing():
    return render_template ('WAREHOUSING.html')



@app.route('/stock')
def stock():
    return render_template('inenventory.html')



@app.route('/tips')
def tips():
    return render_template('business.tips.html')


@app.route('/consultation')
def consutation():
    return render_template('consultation.html')


@app.route('/trending')
def trending():
    return render_template('TRENDING_.html')




@app.route('/faq')
def faq():
    return render_template('FAQS.html')


@app.route('/BI')
def BI():
    return render_template('BI.html')

@app.route('/camera')
def camera():
    return render_template('CAMERA_ROOM.html')



@app.route('/floor_walkers')
def floor_walkers():
    return render_template('floor.walkers.html')


@app.route('/training')
def training():
    return render_template('training.html')



@app.route('/double_check')
def double_check():
    return render_template('DOUBL_CHECKERS.html')


@app.route('/labour')
def labour():
    return render_template('labor.html')

@app.route('/report')
def report():
    return render_template('loss.report.html')



@app.route('/webinars')
def webinars():
    return render_template('webinars.html')



@app.route('/risk')
def risk():
    return render_template('RISKY.html')

@app.route('/chatbot')
def bot():
    return render_template('BOTMAH.html')




@app.route('/portal')
def portal():
    return render_template('portal.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/frontend')
def frontend():
    return render_template('frontendcheck.html')


@app.route('/investigations')
def investigations():
    return render_template('investigation.html')


@app.route('/contact')
def contact():
    return render_template('CONTACT_US.html')

@app.route('/send_mail', methods=['POST'])
def send_mail():
    try:
        # Retrieve form data
        business_type = request.form.get('businessType')
        company_name = request.form.get('companyName')
        company_email = request.form.get('companyEmail')
        project_budget = request.form.get('projectBudget')
        referral_source = request.form.get('referralSource')
        project_details = request.form.get('projectDetails')
        contact_method = request.form.get('contactMethod')

        # Validate critical fields
        if not company_email or not company_name:
            return jsonify(success=False, error="Missing required fields."), 400

        # Package email content
        msg = EmailMessage()
        msg["Subject"] = f"New Contact Request from {company_name}"
        msg["From"] = company_email
        msg["To"] = RECEIVER_EMAIL
        content = f"""
        Business Type: {business_type}
        Company Name: {company_name}
        Company Email: {company_email}
        Project Budget: {project_budget}
        Referral Source: {referral_source}
        Project Details: {project_details}
        Preferred Contact Method: {contact_method}
        """
        msg.set_content(content)

        # Send email via Mailtrap
        with smtplib.SMTP(MAILTRAP_HOST, MAILTRAP_PORT) as server:
            server.starttls()
            server.login(MAILTRAP_USER, MAILTRAP_PASS)
            server.send_message(msg)

        return jsonify(success=True)
    except Exception as e:
        # Log the exception as needed
        return jsonify(success=False, error=str(e)), 500



@app.route('/register', methods=['POST'])
def register():
    # Retrieve form data
    participant_name = request.form.get('participantName')
    participant_email = request.form.get('participantEmail')
    participant_phone = request.form.get('participantPhone')
    webinar_name = request.form.get('webinarName')

    # Validate required fields
    if not (participant_name and participant_email and participant_phone and webinar_name):
        return jsonify(success=False, error="Missing required fields."), 400

    # Compose email content
    subject = f"New Webinar Registration: {webinar_name}"
    content = f"""
Registration Details:
Name: {participant_name}
Email: {participant_email}
Phone: {participant_phone}
Webinar: {webinar_name}
"""
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = participant_email
    msg["To"] = "tonyhuncho997@gmail.com"
    msg.set_content(content)

    try:
        with smtplib.SMTP(MAILTRAP_HOST, MAILTRAP_PORT) as server:
            server.starttls()
            server.login(MAILTRAP_USER, MAILTRAP_PASS)
            server.send_message(msg)
        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=str(e)), 500



if __name__ == '__main__':
    app.run(debug=True, port=7000)
