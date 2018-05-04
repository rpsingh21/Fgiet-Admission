from PIL import Image
from celery.decorators import task

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template

from .way2sms import Sms

@task(name="send_simple_sms")
def send_sms(phone, message):
    sms = Sms()
    res = sms.send(phone,message)
    sms.logout()
    return res

@task(name="send_simple_email")
def send_email(subject,mail, html_template, mail_context, from_email, to_emails):
    template = get_template(html_template)
    html_mail = template.render(mail_context)
    from_email = from_email or settings.EMAIL_HOST_USER
    send_mail(subject, mail, from_email, to_emails,html_message=html_mail)

@task(name="convert_thumbnail_image")
def convert_thumbnail(path, size):
    img = Image.open(path)
    img.thumbnail(size)
    img.save(path, img.format, quality=0)
