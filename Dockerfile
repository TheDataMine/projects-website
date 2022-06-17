FROM python:3.9-slim-bullseye

RUN apt update -y && apt install build-essential libpq-dev -y 

RUN python -m pip install fastapi "uvicorn[standard]" jinja2 aiosql psycopg2-binary --no-binary psycopg2-binary python-dotenv pydantic

WORKDIR /workspace

COPY . .

EXPOSE 8000

ENTRYPOINT ["uvicorn", "website.main:app", "--host", "0.0.0.0", "--reload"]
