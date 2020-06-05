from twilio.rest import Client

account_sid = 'AC5ca2ab180a711c208cacdd6527b78ba4'
auth_token = '9630adc5d4006394a04e1331daa49b72'
client = Client(account_sid, auth_token)

def send_message():
    message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body='ANY MESSAGE',
                                  to='whatsapp:+573023777709'
    )

    print(message.sid)
