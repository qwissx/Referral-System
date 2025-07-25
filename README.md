# Referral-System
Тестовое задание для  Hammer System

## Project
В проекте была реализована простая реферальная система и регистрация по номеру телефона. В качестве веб фреймворка использовался Django (DRF) и для отправки сообщений в телеграмм Telethon.

## Install
```bash
git clone https://github.com/qwissx/Referral-System.git
```

## Run
Скопировать .env.example файл в .env находящийся в корневом каталоге и вставить свои api id и api hash для телеграмм.

Затем необходимо создать образ приложения.
```bash
docker build -f docker/Dockerfile -t referral .
```

После чего запустить контейнер с Postgres (предварительно установив образ postgres:latest).
```bash
docker run --name main \
  -e POSTGRES_USER=main \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=main \
  -p 5432:5432 \
  -d postgres:latest
```

Запускаем контейнер python приложения.
```bash 
docker run --name test -p 8000:8000 weather
```

Загружаем миграции базы данных.
```bash 
docker exec -it test python manage.py migrate
```

После чего приложение будет доступно по хосту http://localhost:8000/.

## Test

Данное приложение я захостил на адрес, который скину лично в телеграмм. Необходимо перейти по адресу /form/account/auth/send-code, после чего пройти регистрацию с нескольких номеров телефона для проверки реферальной системы.
