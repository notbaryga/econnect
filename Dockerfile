FROM python:3.12

RUN mkdir/app

WORKDIR /app

RUN pip install -r requirements.txt

COPY . .

WORKDIR /src

CMD guvicorn main:app --bing=0.0.0.0:8000

