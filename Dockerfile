FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /mypythonapp

COPY requirements.txt /mypythonapp/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /mypythonapp/
