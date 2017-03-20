

from flask import Flask, request
import requests
import json
import traceback
import random


from wit import Wit


CLIENT_ACCESS_TOKEN = '2K7GXJSRTF7B5ZB74PNZBZQPGFYIIRKC'
token = "EAAD0FIbuQqcBAMpc3F8B1W3qZBoUwjhzYn20WtFC9nVE8b7WZCbNypK3znS7mYBqijvvpvqds14UXHCqV1EwLLnC9q5ZAhmPt0h7SVpAQL65e2oRzKyurb9QYDSdXKmbV9cuP6IDiNxy63SMKPGZBNpQRy8ZB9MOjLbkJi8SmeQZDZD"


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
        data = request.json
        if data['object'] == "page":
            for entry in data['entry']:
                pageID = entry['id']
                for msg in entry['messaging']:
                    if msg['message']:
                        sender = msg['sender']['id']
                        if len(msg['message']) < 4:
                            message = msg['message']['text']

                            res = client.converse(sender, message, {})
                            if res['msg']:
                                reply (sender, res['msg'])
                                return "ok"
                            return "ok"
                        return "ok"
                    return "ok"
    except Exception as e:
        print traceback.format_exc() # something went wrong
  elif request.method == 'GET': # For the initial verification
    return request.args.get('hub.challenge')
    return "ok"


client = Wit(access_token=CLIENT_ACCESS_TOKEN)


if __name__ == '__main__':
  app.run(debug=True)
