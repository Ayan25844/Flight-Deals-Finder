
import os
from twilio.rest import Client

auth_token = os.environ.get("AUTH_TOKEN")
account_sid = os.environ.get("ACCOUNT_SID")

VIRTUAL_NUMBER = os.environ.get("VIRTUAL_NUMBER")
VERIFIED_NUMBER = os.environ.get("VERIFIED_NUMBER")

class NotificationManager:
    def __init__(self,message):
        self.client = Client(account_sid, auth_token)
        
        message = self.client.messages.create(
            body=message,
            to=VERIFIED_NUMBER,
            from_=VIRTUAL_NUMBER
        )
        