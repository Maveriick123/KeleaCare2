import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from .llm import *

app = FastAPI()

last_response = {"result": None}


app.mount("/static", StaticFiles(directory="app/static"), name="static")

class MessageRequest(BaseModel):
    text: str

@app.get("/")
async def read_index():
    return FileResponse("app/static/index.html")

@app.post("/api/send-message")
async def sendMessage(request: MessageRequest):
    """user_input = request.text
    #bd.add_vectors(get_emotions(user_input))
    return {"result": chat(user_input)}"""
    global last_response
    user_input = request.text
    response = chat(user_input)
    tmp = get_emotions(user_input)
    last_response["result"] = response
    return last_response

@app.get("/api/get-response")
async def receiveMessage():
    return last_response 


if __name__ == '__main__':
    uvicorn.run(app='app.main:app', port=8000)

""" Insertar un embedding
embedding = np.random.rand(512).astype(np.float32)  
asyncio.run(insert_embedding("Hola, esto es una prueba", embedding))"""





