from secrets import *
from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_recv_msg():
    """Receive and respond to messages for Wikipedia queries"""
    resp = MessagingResponse()
    resp.message("Ahoy! Thanks so much for your message!")
    return str(resp)

if __name__ == "__main__":
    # client = Client(TWILIO_SID, TWILIO_AUTH)
    # message = client.messages \
    #     .create(
    #         body="Segmentation fault",
    #         from_='+12056512620',
    #         to='+14809391551'
    #     )
    app.run(debug=True)