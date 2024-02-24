from flask import Flask,render_template
from dotenv import load_dotenv
import os
from mail_lib import mail
from mail_lib import send_mail
from mail_part import mail_app


load_dotenv()

app = Flask(__name__)
app.config["MAIL_SERVER"] = os.environ["MAIL_SERVER"]
app.config["MAIL_PORT"] = os.environ["MAIL_PORT"]
app.config["MAIL_USE_SSL"] = os.environ["MAIL_USE_SSL"]
app.config["MAIL_USERNAME"] = os.environ["MAIL_USERNAME"]
app.config["MAIL_PASSWORD"] = os.environ["MAIL_PASSWORD"]
mail.init_app(app)

app.register_blueprint(mail_app)

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def error_404(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run()
