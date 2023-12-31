import logging

import requests


logger = logging.getLogger(__name__)


def get_google_credentials(auth_token: str) -> dict[str, str]:
    """
    Получение access_tokken, refresh_token google oAuth2.

    Токены получается из accounts сервиса.
    Аутентификация через token auth_token.
    """
    try:
        url = 'http://accounts:8000/api/v1/accounts/users/google/token/'

        response = requests.get(
            url,
            headers={
                'Authorization': ('Token ' + auth_token)
            }
        )
        if response.status_code == 200:
            return response.json()

        logger.error(
            'Request failed with status code: %s. Response data: %s',
            response.status_code,
            response.json()
        )
    except requests.RequestException as e:
        logger.error('Error during request: %s', e)
