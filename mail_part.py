from flask import (Blueprint,
                   render_template,
                   request,
                   redirect)
from mail_lib import send_mail

mail_app = Blueprint('mail_app', __name__,
                     template_folder='templates')

@mail_app.route("/send",methods=["POST"])
def get_message():
    form_data = request.form
    text = f"""До Вас звертається {form_data.get('email')}
Текст повідомлення
{form_data.get('text')}"""
    send_mail("Нова заявка на сайті",
              body=text,
              recipients=['deadbuddy02@gmail.com',
                          'accbucha@gmail.com',
                          'egen13@ukr.net'])
    return redirect("/thanks")

@mail_app.route("/thanks")
def thanks():
    return render_template("thanks.html")
