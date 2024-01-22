import os
from twilio.rest import Client
account_sid = os.environ['AC4f4167a70886d42a7cc154f0ce801da3']
auth_token = os.environ['5456013fe7de07e975864631d0a24ad4']

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Hello there from Twilio SMS API',
         from_ ="+12176287069",
         to ="+917507008076"
     )

print(message.sid)