# celery-rabbitmq-flask-docker-example
A simple demo on using celery, rabbitmq, and flask using docker containers

# Overview
This is a very simple, basic on how to set up a flask app that uses celery for 
async tasks and rabbitmq as a message broker. It ties them all together using 
docker and docker-compose. I made this because there are a million demos and 
tutorials out there, but some are needlessly complex in order to get a basic 
working application up and running. This is the bare minimum and easy to set up.

# Instructions

#### Note: This demo assumes you already have docker and docker-compose installed on your machine.
### 1. Clone the repo

`git clone git@github.com:juggernautrises/celery-rabbitmq-flask-docker-example.git`

### 2. Build and run!
Change to the cloned directory

`cd celery-rabbitmq-flask-docker-example`

Build and bring the containers up

`docker-compose up --build`

### 3. Make an API call and verify the result

The app just adds two numbers and returns the result. Flask takes the arguments and runs the addition procedure via a celery task. The result of the task is returned in the Flask response. In this case, the numbers are 5 and 10:

` curl "http://localhost:5000/add?first=5&second=10"`
```
{
  "result": 15
}
```
