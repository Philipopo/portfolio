import yagmail
from django.conf import settings

def send_email(subject, recipient, content):
    yag = yagmail.SMTP(settings.YAGMAIL_USER, settings.YAGMAIL_PASSWORD)
    yag.send(
        to=recipient,
        subject=subject,
        contents=content
    )