# Docker Workshop --- Flask + Redis

Практична робота присвячена контейнеризації простого веб-додатка на
Flask, який використовує Redis для зберігання лічильника переглядів
сторінки. Проєкт складається з двох сервісів, що запускаються за
допомогою Docker Compose.

## 📁 Структура проєкту

    docker_workshop/
     ├── app.py
     ├── Dockerfile
     ├── docker-compose.yml
     ├── requirements.txt

## 🚀 Функціональність

Під час кожного оновлення сторінки додаток збільшує лічильник
переглядів, який зберігається у Redis.

## 🧩 Використані технології

-   Python 3.9\
-   Flask 3.1.0\
-   Redis 7\
-   Docker / Docker Compose

## 📌 Файли проєкту

### app.py

``` python
from flask import Flask
import redis, os

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def hello():
    count = redis_client.incr('hits')
    return f"Hello from Docker! This page has been viewed {count} times."

if __name__ == '__main__':
    port = int(os.environ.get('APP_PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

### requirements.txt

    flask==3.1.0
    redis==7.0.1

### Dockerfile

``` dockerfile
FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
```

### docker-compose.yml

``` yaml
version: "3.8"
services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - APP_PORT=5000
    depends_on:
      - redis
  redis:
    image: redis:7
```

## ▶️ Запуск

    docker compose up --build

## ⏹ Зупинка

    Ctrl + C
    docker compose down

## 🖼 Скриншоти

Нижче розміщені скріншоти, що демонструють роботу проєкту.

### 1. Project Structure

<p align="center"> 
 <img src="./Image/Project%20Structure.png" width="1200" alt="operators list"> 
</p>

Опис: структура папок та файлів проєкту.

### 2. Docker Compose Build Output

<p align="center"> 
 <img src="./Image/Docker%20Compose%20Build%20Output_1.png" width="1200" alt="operators list"> 
</p>

Опис: процес складання контейнерів через `docker compose up --build`.

### 3. Running Containers in Terminal

<p align="center"> 
 <img src="./Image/Docker%20Compose%20Build%20Output_2.png" width="1200" alt="operators list"> 
</p>

Опис: лог запуску Flask та Redis контейнерів.

### 4. Docker Desktop — Running Containers

<p align="center"> 
 <img src="./Image/Docker%20Desktop%20—%20Running%20Containers.png" width="1200" alt="operators list"> 
</p>

Опис: відображення контейнерів у Docker Desktop.

### 5. Application Output — Page View Counter

<p align="center"> 
 <img src="./Image/Application%20Output%20—%20Page%20View%20Counter_1.png" width="1200" alt="operators list"> 
</p>

<p align="center"> 
 <img src="./Image/Application%20Output%20—%20Page%20View%20Counte_2.png" width="1200" alt="operators list"> 
</p>

Опис: сторінка, де показано лічильник переглядів.

### 6. Application Logs — Requests

<p align="center"> 
 <img src="./Image/Application%20Logs%20—%20Requests.png" width="1200" alt="operators list"> 
</p>

Опис: логування HTTP-запитів від Flask-контейнера.

### 7. Docker Compose Down Output

<p align="center"> 
 <img src="./Image/Docker%20Compose%20Down%20Output.png" width="1200" alt="operators list"> 
</p> 

Опис: коректне вимкнення та видалення контейнерів.

## 📘 Висновки

У ході виконання практичної роботи було створено Docker-образ
Flask-додатка, налаштовано сервіс Redis та реалізовано запуск застосунку
через Docker Compose. Було сформовано міні-систему з двох контейнерів,
що взаємодіють між собою у спільній мережі.
