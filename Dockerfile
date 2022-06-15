FROM python:3.9-slim-bullseye

RUN python -m pip install fastapi "uvicorn[standard]" jinja2 aiosql

WORKDIR /workspace

COPY . .

EXPOSE 8000

ENTRYPOINT ["uvicorn", "website.main:app", "--host", "0.0.0.0", "--reload"]
