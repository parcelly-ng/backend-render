import json
import requests


import os
from dotenv import load_dotenv
load_dotenv()


def send(number, message):
    headers = {
        'Authorization': os.getenv('whatsappaccess'),
        'Content-Type': 'application/json',
    }

    data = {
        "messaging_product": "whatsapp",
        "preview_url": False,
        "recipient_type": "individual",
        "to": number,
        "type": "text",
        "text": {
                "body": message
        }
    }
    a = json.dumps(data)
    print('sending')

    b = requests.post('https://graph.facebook.com/v17.0/1689306551511250/messages',
                      headers=headers,
                      data=a)
    print(b.text)
