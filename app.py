
from flask import Flask, request
import requests
import json
import traceback
import random


from wit import Wit


CLIENT_ACCESS_TOKEN = '2K7GXJSRTF7B5ZB74PNZBZQPGFYIIRKC'
token = "EAAD0FIbuQqcBAD21V7lMhM4DG0zUD4eLBqCa0J0JnDZARrGrkEXtR4ZCmZAn4dUJ3GzA6JB5Y1j8tCtKN9q7TgcHGViZAUSdjyNirYGapRSJEC85RehaEfEuRFf6ZCMnRJ1WEehQZAwr5CRaPePOxnRNROtocBnjRDXHF6ZAA1FMgZDZD"
 

app = Flask(__name__)

def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + token, json=data)

@app.route('/', methods=['GET', 'POST'])
def webhook():
  if request.method == 'POST':
    try:
      data = json.loads(request.data)
      text = data['entry'][0]['messaging'][0]['message']['text'] # Incoming Message Text
      sender = data['entry'][0]['messaging'][0]['sender']['id'] # Sender ID
	  
      res = client.converse(sender, text, {})
      reply (sender, res ['msg'])

    except Exception as e:
      print traceback.format_exc() # something went wrong
  elif request.method == 'GET': # For the initial verification
    return request.args.get('hub.challenge')


client = Wit(access_token=CLIENT_ACCESS_TOKEN)
 

if __name__ == '__main__':
  app.run(debug=True)
