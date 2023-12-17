import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# Youtube
API_SERVICE_NAME = 'youtube'

API_VERSION = 'v3'

# Domain
DOMAIN = os.getenv('DOMAIN')

PREFIX_DOMAIN = os.getenv('PREFIX_DOMAIN')
