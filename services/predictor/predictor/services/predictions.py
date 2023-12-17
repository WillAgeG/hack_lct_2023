import logging

import requests
from requests import Response


logger = logging.getLogger(__name__)


def insert_prediction(
    predict_id: str | int,
    predict: dict,
    auth_token: str
) -> Response:
    """
    Отправить запрос создание предсказания.
    """
    accounts_domain = 'http://accounts:8000'
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


def get_youtube_data(
    auth_token: str
) -> Response:
    """
    Получить спаршенные данные с youtube.
    """
    url = 'http://parser:8000/api/v1/parser/'
    data = {
        'auth_token': auth_token
    }

    response = requests.post(
        url,
        json=data
    )

    if response.status_code != 200:
        error_msg = (
            'Request failed with status code: %s. Response data: %s',
            response.status_code,
            response.json()
        )
        logger.error(error_msg)
        raise ValueError(error_msg)

    return response.json()


def get_prediction_from_ai(youtube_data: dict) -> dict[dict, dict, dict]:
    """Получить спрогнозированные данные."""

    prediction = {
        'result': 'result',
        'result2': 'result',
        'result3': 'result'
    }
    return prediction


async def create_prediction(
    auth_token: str,
    predict_id: str
) -> None:
    """
    Таск селери создание предсказания.

    Предсказание будет создано и через accounts передано в бд.
    """
    youtube_data = get_youtube_data(
        auth_token
    )
    prediction_data = get_prediction_from_ai(youtube_data)
    insert_prediction(
        predict_id,
        prediction_data,
        auth_token
    )
