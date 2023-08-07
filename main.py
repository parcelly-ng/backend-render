from typing import Union


from fastapi import FastAPI, Request, Response
from send_message import send_out


app = FastAPI()



@app.get("/whatsapp")
def whatsapp_webhook(request: Request):

    return int(request.query_params["hub.challenge"])


@app.post("/whatsapp")
async def whatsapp_process(request: Request):
    note= await request.json()
    print(note)
    number = note['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']
    message1=note.get('entry')[0].get('changes')[0].get('value').get('messages')[0].get('text').get('body')
    message2=''
    return send_out.send(number,message1)
    


    return Response('hello',status_code=200)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}




