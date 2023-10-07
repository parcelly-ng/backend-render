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
    response = requests.request(
        "POST", url, headers=headers, data=json.dumps(payload))

    res = json.loads(response.text.encode('utf8'))
    if len(res) == 0:
        return False
    else:
        return res[0]['session']


def add(number, session='A', url=url, headers=headers):
    payload = {
        "operation": "insert",
        "schema": "backend",
        "table": "session",
        'records': [
            {
                'phone': int(number),
                'session': session
            }
        ],
    }
    response = requests.request(
        "POST", url, headers=headers, data=json.dumps(payload))


def update(number, session='A', url=url, headers=headers):
    payload = {
        "operation": "update",
        "schema": "backend",
        "table": "session",
        'records': [
            {
                'phone': int(number),
                'session': session
            }
        ],
    }
    response = requests.request(
        "POST", url, headers=headers, data=json.dumps(payload))


def add_order(number, order, url=url, headers=headers):
    payload = {
        "operation": "update",
        "schema": "backend",
        "table": "session",
        'records': [
            {
                'phone': int(number),
                'order': order
            }
        ],
    }
    response = requests.request(
        "POST", url, headers=headers, data=json.dumps(payload))


def check_order(number, url=url, headers=headers):
    payload = {
        "operation": "search_by_hash",
        "schema": "backend",
        "table": "session",
        "hash_values": [int(number)],
        "get_attributes": ['order',]
    }
    response = requests.request(
        "POST", url, headers=headers, data=json.dumps(payload))

    res = json.loads(response.text.encode('utf8'))
    if len(res) == 0:
        return False
    else:
        return res[0]['order']
