from __future__ import print_function

import json
from flask import Flask, request
import requests


from wit import Wit


CLIENT_ACCESS_TOKEN = '2K7GXJSRTF7B5ZB74PNZBZQPGFYIIRKC'
ACCESS_TOKEN = "EAAD0FIbuQqcBANEw2ZBwnte4MymXmZBwaC3s5saHfinJTAsEzPhHymUosdROb8ejgzJ0IQZAm9nZC5olje770hNC704Cl9wu6zwZAhTttoFzHqqZCUQc9pyUHucwbj7pPaTmBf11ZAFYdZAb1xIfRFSeZAmMi0VSuL4MO9o4rt7yvvQZDZD"
 
	
	




app = Flask(__name__)

 
#
#def send(request, response):
#    """
#    Sender function
#    """
#    # We use the fb_id as equal to session_id
#    fb_id = request['session_id']
#    text = response['text']
#    # send message
#    reply(fb_id, text)
#	

def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    return resp.content


@app.route('/', methods=['GET'])
def handle_verification():
    return request.args['hub.challenge']


@app.route('/', methods=['POST'])
def handle_incoming_messages():
	data = request.json
	if data['object'] == "page":
		for entry in data['entry']:
			pageID = entry['id']
			for msg in entry['messaging']:
				if msg['message']:
					sender = msg['sender']['id']
					message = msg['message']['text']


					context0 = {}
					res = client.converse(sender, message, context0)

					#reply (sender, str(res))
					reply (sender, res ['msg'])
					#reply (sender, res ['quickreplies'])
					return "ok"
				else:
					return "ok"
	return "ok"

client = Wit(access_token=CLIENT_ACCESS_TOKEN)
 
if __name__ == '__main__':
    app.run(debug=True)
