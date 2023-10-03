from typing import Union


from fastapi import FastAPI, Request, Response
from send_message import main as brain
from session import main as session


app = FastAPI()



@app.get("/whatsapp")
def whatsapp_webhook(request: Request):

    return int(request.query_params["hub.challenge"])


@app.post("/whatsapp")
async def whatsapp_process(request: Request):
    note= await request.json()
    print(note)
    try:
        number = note['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']
        message1=note.get('entry')[0].get('changes')[0].get('value').get('messages')[0].get('text').get('body')
        ses=session.check(number)
        if ses==False:
            session.add(number)
            brain.brain(number,message1)
        else:
            brain.brain(number,message1)
    except Exception as e:
        print('not important')
        print(e)
    return Response('hello',status_code=200)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}




