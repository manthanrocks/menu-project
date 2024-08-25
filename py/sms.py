from twilio.rest import Client

def send_text_message():
   
    text_message = input('Enter your message: ')
    
    
    account_sid = ''
    auth_token = 'f'
    
    # Create a Twilio client
    client = Client(account_sid, auth_token)
    
   
    message = client.messages.create(
        body=text_message,
        from_='',
        to=''
    )
    
   
    print(f'Message SID: {message.sid}')
