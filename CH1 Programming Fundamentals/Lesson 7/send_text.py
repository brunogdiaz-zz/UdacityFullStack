from twilio.rest import TwilioRestClient

account_sid = 'AC7176b76dd02571da$$$$$$$$$'
auth_tok = 'ceb801dfbebc9c8$$$$$$$$$$$$$'

client = TwilioRestClient(account_sid,auth_tok)

message = client.sms.messages.create(body='NOOOOO', to='+1305$$$$$$$', from_='+1786$$$$$$$')

print message.sid