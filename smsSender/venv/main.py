from twilio.rest import Client

account_sid = 'ACCOUNT_SID'
auth_token = 'AUTH_TOKEN'

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body="Message Text",
         from_='+EXT_NUMBER_FROM',
         to='+EXT_NUMBER_TO'
     )

# +12059973790
print(message.sid)
