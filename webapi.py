from secrets import *
from flask import Flask, request
from string_processing.processor import get_query_list, get_page_summary
from twilio.twiml.messaging_response import MessagingResponse
# from twilio.rest import Client

app = Flask(__name__)

"""
{
    phoneNumber: {
        lastTextSid: "",
        lastQueryResult: ""
    }
}
"""
userdict = {}

@app.route("/sms", methods=['GET', 'POST'])
def sms_recv_msg():
    """Receive and respond to messages for Wikipedia queries"""
    resp = MessagingResponse()
    form = request.form
    print(form)
    if len(form['Body']) > 8 and form['Body'][:6].lower() == "search":
        qlist = get_query_list(form['Body'][7:])
        message = ""
        i = 0
        message += "-\n"
        for item in qlist:
            i += 1
            message += str(i) + ". " + qlist[i - 1] + "\n"
        userdict[form['From']] = {
            'lastTextSid': form['MessageSid'],
            'lastQueryResult': qlist
        }
        resp.message(message)
    elif form['Body'].isnumeric():
        body = int(form['Body'])
        qlist = userdict[form['From']]['lastQueryResult']
        if body >= 1 and body <= len(qlist):
            message = get_page_summary(qlist, body - 1)
            userdict[form['From']] = {
                'lastTextSid': form['MessageSid'],
                'lastQueryResult': qlist
            }
            resp.message(message)
        else:
            resp.message("Sorry, I couldn't understand")
    else:
        resp.message("Sorry, I couldn't understand")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)