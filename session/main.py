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


def check(number, message, url=url, headers=headers):
    payload = {
        "operation": "search_by_hash",
        "schema": "dev",
        "table": "dog",
        "hash_values": [number],
        "get_attributes": ['session']
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))


def add():
    pass
