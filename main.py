from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.context_processor
def copyright():
    return {'current_year': datetime.now().year}


if __name__ == "__main__":
    app.run(debug=True)