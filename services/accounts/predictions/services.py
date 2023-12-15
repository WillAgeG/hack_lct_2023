import logging

import requests
from requests import Response
# from django.conf import settings

logger = logging.getLogger(__name__)


def start_predicting(
    predict_id: str | int,
    auth_token: str
) -> Response:
    """
    Отправить запрос создание предсказания.
    """
    url = 'http://predictor:8000/api/v1/predictor/'
    data = {
        'predict_id': str(predict_id),
        'auth_token': auth_token
    }

    response = requests.post(
        url,
        json=data
    )

    if response.status_code != 200:
        logger.error(
            'Request failed with status code: %s. Response data: %s',
            response.status_code,
            response.json()
        )

    return response
