from typing import Union

from fastapi import FastAPI, Request, Response

app = FastAPI()



@app.get("/whatsapp")
def whatsapp_webhook(request: Request):

    return int(request.query_params["hub.challenge"])


@app.post("/whatsapp")
async def whatsapp_process(request: Request):
    note= await request.json()
    print(note)

    return Response('hello',status_code=200)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}




