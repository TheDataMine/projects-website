from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory='templates/')

@app.get("/")
async def root(request: Request):
    accept = request.headers.get("accept")
    hello_world = {"message": "hello world"}

    if accept.split("/")[1] == 'json':
        return hello_world

    if len(accept.split(",")) > 1 or accept.split("/")[1] == 'html':
        response = templates.TemplateResponse("index.html", {"request": request, "payload1": hello_world}) 
        return response

