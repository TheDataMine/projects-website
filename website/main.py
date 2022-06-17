from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from dotenv import load_dotenv
import psycopg2
import aiosql
import os
from pydantic import BaseModel


app = FastAPI()
templates = Jinja2Templates(directory='templates/')

class Company(BaseModel):
    name: Optional[str]
    address: str


@app.get("/hello/{name}")
async def root(request: Request, name: str):
    accept = request.headers.get("accept")
    hello_world = {"message": f"hello {name}"}

    if accept.split("/")[1] == 'json':
        return hello_world

    if len(accept.split(",")) > 1 or accept.split("/")[1] == 'html':
        response = templates.TemplateResponse("index.html", {"request": request, "payload1": hello_world}) 
        return response

@app.get("/companies")
async def get_companies(request: Request):
    load_dotenv()

    conn = psycopg2.connect(f"dbname=tdm_main user=rdonly password={os.getenv('PG_PASSWORD')} host=db.tdm.geddes.rcac.purdue.edu")
    queries = aiosql.from_path("queries.sql", "psycopg2")

    companies = [v[0] for v in queries.get_all_companies(conn)]

    companies = [Company(name=v) for v in companies]
    print(f"{companies=}")
    
    # inspecting request object for fun
    print(f"{request.method=}")
    print(request.url)
    print(request.headers)
    print(request.query_params)
    print(request.path_params)
    print(request.client)
    print(request.cookies)
    print(request.json())

    accept = request.headers.get("accept")
    hello_world = {"message": "hello world"}

    if accept.split("/")[1] == 'json':
        return companies

    if len(accept.split(",")) > 1 or accept.split("/")[1] == 'html':
        response = templates.TemplateResponse("companies.html", {"request": request, "payload1": companies}) 
        return response

