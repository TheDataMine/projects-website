from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from dotenv import load_dotenv
import psycopg2
import aiosql
import os


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

@app.get("/companies")
async def get_companies(request: Request):
    load_dotenv()

    conn = psycopg2.connect(f"dbname=tdm_main user=rdonly password={os.getenv('PG_PASSWORD')} host=db.tdm.geddes.rcac.purdue.edu")
    queries = aiosql.from_path("queries.sql", "psycopg2")

    companies = [v[0] for v in queries.get_all_companies(conn)]
    print(type(companies))
    print(companies)

    accept = request.headers.get("accept")
    hello_world = {"message": "hello world"}

    if accept.split("/")[1] == 'json':
        return hello_world

    if len(accept.split(",")) > 1 or accept.split("/")[1] == 'html':
        response = templates.TemplateResponse("companies.html", {"request": request, "payload1": companies}) 
        return response