# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("AC4f4167a70886d42a7cc154f0ce801da3", "5456013fe7de07e975864631d0a24ad4")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+917507008076",
                       from_="+12176287069",
                       body="Hello from Python!")