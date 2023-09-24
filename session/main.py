import requests
import json


import os
from dotenv import load_dotenv
load_dotenv()


import redis

r = redis.Redis(
  host='redis-17505.c309.us-east-2-1.ec2.cloud.redislabs.com',
  port=17505,
  password=os.getenv('reddis_password'))


# url = "https://botdb-parcellydb.harperdbcloud.com"

# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': os.getenv('db')
# }


# def check(number, url=url, headers=headers):
#     payload = {
#         "operation": "search_by_hash",
#         "schema": "backend",
#         "table": "session",
#         "hash_values": [int(number)],
#         "get_attributes": ['session',]
#     }
#     response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

#     print(response.text.encode('utf8'))


# def add():
#     pass
