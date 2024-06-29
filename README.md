## Introduction 
A dockerized flask application with asynchronous task queue using Celery and Redis. The application is a simple REST API that accepts a POST request with a JSON payload and returns a JSON response. The application is dockerized and can be run using docker-compose. The application uses Celery and Redis for asynchronous task queue with Celery and with load testing with locust. 

```commandline
docker compose up --build
```
To restart all the services, use the following command:
```commandline
docker compose stop 
```