import requests
import json


import os
from dotenv import load_dotenv
load_dotenv()





url = "https://botdb-parcellydb.harperdbcloud.com"

headers = {
    'Content-Type': 'application/json',
    'Authorization': os.getenv('db')
}


def check(number, url=url, headers=headers):
    payload = {
        "operation": "search_by_hash",
        "schema": "backend",
        "table": "session",
        "hash_values": [int(number)],
        "get_attributes": ['session',]
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    print(response.text.encode('utf8'))


def add():
    pass
