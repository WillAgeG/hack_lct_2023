from celery import Celery

from .configs import HOST_REDIS, PORT_REDIS

app = Celery(
    'predictor.core.celery',
    broker=f'redis://{HOST_REDIS}:{PORT_REDIS}/0',
    backend=f'redis://{HOST_REDIS}:{PORT_REDIS}/0',
    include=['predictor.core.celery']
)

app.conf.broker_connection_retry_on_startup = True

app.conf.task_routes = {
    'predictor.services.predictions.create_prediction': {'queue': 'my_queue'}
}

app.conf.timezone = 'Asia/Tokyo'
