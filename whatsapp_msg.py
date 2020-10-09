#first install twilio library
#pip install twilio
from twilio.rest import Client #Import twilio library

# Main function
def Sent_Message(event=None, context=None):

    # Here we put the credencials ofTwilio
    twilio_sid = 'XXXXXXXXXXXXXXXX'
    auth_token = 'XXXXXXXXXXXXXXXX'

    #make the conecction
    whatsapp_client = Client(twilio_sid, auth_token)

    # in this directory save the destiny numbers and the Names(this is for the message)  
    contact_directory = {'Camilo':'+57XXXXXXXX','Juan':'+57XXXXXXXX'}

    for key, value in contact_directory.items():            #For cicle for every value in the directory
        #message to send
        msg_loved_ones = whatsapp_client.messages.create(
                body = 'Hola {} !'.format(key),
                from_= 'whatsapp:+14155238886',
                to='whatsapp:' + value,

            )
        #print in console the message
        print(msg_loved_ones.sid)