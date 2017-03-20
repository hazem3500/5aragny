# from __future__ import print_function

# import json
# from flask import Flask, request
# import requests


# from wit import Wit


# CLIENT_ACCESS_TOKEN = '2K7GXJSRTF7B5ZB74PNZBZQPGFYIIRKC'
# ACCESS_TOKEN = "EAAEiCmoan6YBADgzCXxzLQZC3HninZAFmwjsqDFcJlXR6G8aYI6xZA7ZBfPngY9IP7xlojZCU0InMle1ZCWoP3yD1mpXCNFfdrIhfUl7mfJMHiWlRmvdPIZAErILzMUlG0g3CalLkZANVnKWfYHxxJhZCbRCdXfZBwf822Ij2o8FMIngZDZD"
 
	
	




# app = Flask(__name__)

 
# #
# #def send(request, response):
# #    """
# #    Sender function
# #    """
# #    # We use the fb_id as equal to session_id
# #    fb_id = request['session_id']
# #    text = response['text']
# #    # send message
# #    reply(fb_id, text)
# #	

# def reply(user_id, msg):
#     data = {
#         "recipient": {"id": user_id},
#         "message": {"text": msg}
#     }
#     resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
#     return resp.content

# @app.route('/', methods=['GET'])
# def asd():
# 	return "Hello world"
	
# @app.route('/webhook', methods=['GET'])
# def handle_verification():
#     return request.args['hub.challenge']


# @app.route('/webhook', methods=['POST'])
# def handle_incoming_messages():
# 	data = request.json
# 	if data['object'] == "page":
# 		for entry in data['entry']:
# 			pageID = entry['id']
# 			for msg in entry['messaging']:
# 				if msg['message']:
# 					sender = msg['sender']['id']
# 					message = msg['message']['text']


# 					context0 = {}
# 					res = client.converse(sender, message, context0)

# 					#reply (sender, str(res))
# 					reply (sender, res ['msg'])
# 					#reply (sender, res ['quickreplies'])
# 					return "ok"
# 				else:
# 					return "ok"
# 	return "ok"


# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, request
import requests
import json
import traceback
import random


from wit import Wit


CLIENT_ACCESS_TOKEN = '2K7GXJSRTF7B5ZB74PNZBZQPGFYIIRKC'
token = "EAAD0FIbuQqcBAIBnuVDLivMvwj5V2nZAC89qxBF66vxzRutSsNUSFQQcV2nuIGU2aQhIC0qBeHmSfHQ6LBz1hAJrQKh0MyKHkYd8nKUx4QDsf4ZCQfjwsaJ069t7LdLgt0ZCqJIDHWnxAfEi6im2L7cjxgdPd1afL0jZAPlPHgZDZD"
 

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
