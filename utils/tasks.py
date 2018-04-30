from PIL import Image
from celery.decorators import task
from .way2sms import Sms

@task(name="send_simple_sms")
def send_sms(phone, message):
    sms = Sms()
    res = sms.send(phone,message)
    sms.logout()
    return res

@task(name="convert thumbnail image")
def convert_thumbnail(path, size):
    img = Image.open(path)
    img.thumbnail(size)
    img.save(path, img.format, quality=0)
