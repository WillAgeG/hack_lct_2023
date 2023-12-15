import logging

import requests
from requests import Response

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task(name='create_prediction')
def create_prediction():
    pass


def insert_prediction(
    predict_id: str | int,
    predict: dict,
    auth_token: str
) -> Response:
    """
    Отправить запрос создание предсказания.
    """
    accounts_domain = 'http://accounts:8000/'
    url = f'{accounts_domain}/api/v1/accounts/insert_predictions/{predict_id}/'
    data = {
        'predict': predict
    }

    response = requests.patch(
        url,
        json=data,
        headers={
            'Authorization': ('Token ' + auth_token)
        }
    )

    if response.status_code != 200:
        logger.error(
            'Request failed with status code: %s. Response data: %s',
            response.status_code,
            response.json()
        )

    return response
