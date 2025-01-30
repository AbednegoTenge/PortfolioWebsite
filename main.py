from flask import Flask, render_template, request
from smtplib import SMTP
import os

app = Flask(__name__)

EMAIL = os.environ.get('email')
PASSWORD = os.environ.get('password')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        email = request.form.get('email')
        message = request.form.get('message')
        subject = request.form.get('subject')
        send_message = f"Subject: {subject}\n\n{message}"
        try:
            with SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(EMAIL, PASSWORD)
                connection.sendmail(from_addr=EMAIL,
                                    to_addrs=email,
                                    msg=send_message)
                print("Email sent successfully")
        except Exception as e:
            print(f"Error sending email: {e}")
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)