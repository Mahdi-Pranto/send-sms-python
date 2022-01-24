#My_trail_number : +16205665858

from twilio.rest import Client

account_sid = "" # put your ACCOUNT SID number from twilio
auth_token = "" # put your AUTH TOKEN from twilio
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="This is a message I send to you in python 😁", # the message you want to send
    from_="+16205665858", # your number
    to="+8801991308892" # the number you want to send message
)
print(message.sid)
