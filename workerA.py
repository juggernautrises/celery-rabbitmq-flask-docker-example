from celery import Celery

# Celery configuration
CELERY_BROKER_URL = 'amqp://rabbitmq:rabbitmq@rabbit:5672/'
CELERY_RESULT_BACKEND = 'rpc://'

# Initialize Celery
celery = Celery('workerA', broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)


@celery.task(queue='workerA')
def add_nums(a, b):
    return a + b
