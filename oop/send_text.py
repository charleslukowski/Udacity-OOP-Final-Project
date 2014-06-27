# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC153f15880e03562f510d5375d0da11a4"
auth_token  = "70d8eafe285dfd7bef8b0d9a8daf002c"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Sending you a message with a program on the commputer!.. only works with my phone number though!",
    to="+17402228520",
    from_="+17403704423")
print message.sid