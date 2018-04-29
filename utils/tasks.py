from __future__ import absolute_import, unicode_literals
from celery.decorators import task
from .way2sms import Sms

@task(name="send_simple_sms")
def send_sms(phone, message):
    sms = Sms()
    res = sms.send(phone,message)
    sms.logout()
    return res
