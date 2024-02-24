from flask_mail import Mail
from flask_mail import Message
import os

mail = Mail()

def send_mail(title,
              body,
              recipients=[]):
    msg = Message(title,
                  sender=os.environ["MAIL_USERNAME"],
                  body=body,
                  recipients=recipients)
    mail.send(msg)

