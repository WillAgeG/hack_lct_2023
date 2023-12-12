import logging

import requests

from ..core.configs import ACCOUNTS_DOMAIN

logger = logging.getLogger(__name__)


def get_google_tokens(auth_token: str) -> dict[str, str]:
    """
    Получение access_tokken, refresh_token google oAuth2.

    Токены получается из accounts сервиса.
    Аутентификация через token auth_token.
    """
    try:
        response = requests.get(
            'http://' + ACCOUNTS_DOMAIN + '/users/google/token/',
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
