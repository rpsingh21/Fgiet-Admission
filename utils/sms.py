from twilio.rest import Client
from fgietAdmission.secret import twilio

def send_sms(phone, mgs):
    client = Client(twilio["account_sid"], twilio["auth_token"])
    message = client.messages.create(
        to = phone,
        from_ = twilio["phone_no"],
        body = mgs
    )
    print(twilio["account_sid"], twilio["auth_token"])