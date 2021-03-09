FROM tiangolo/uvicorn-gunicorn:python3.8

COPY ./barrel /app

ENV MODULE_NAME="barrel.barrel"
ENV VARIABLE_NAME="app"

COPY ./requirements.txt /app
RUN python3 -m pip -U pip\
    python3 -m pip install -U -r requirements.txt