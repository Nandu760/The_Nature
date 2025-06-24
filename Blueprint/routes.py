from flask import Blueprint, render_template, request, redirect, flash
from flask_mail import Message
from Blueprint.extensions import mail

blueprint = Blueprint('blueprint', __name__)

@blueprint.route('/')
def home():
    return render_template('Nature.html')

@blueprint.route('/Nature', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    try:
        msg = Message(
            subject=f"Message from {name}",
            sender=email,
            recipients=['jangidnisha83@gmail.com'],  # your receiving email
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        )
        mail.send(msg)
        flash("✅ Message sent successfully!", "alert alert-success")
    except Exception as e:
        print("Mail send error:", e)
        flash("❌ Failed to send message. Try again.", "alert alert-danger")

    return redirect('/')