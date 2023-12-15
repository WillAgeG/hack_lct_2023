import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# Domain
DOMAIN = os.getenv('DOMAIN')

PREFIX_DOMAIN = os.getenv('PREFIX_DOMAIN')

# Celery
HOST_REDIS = os.getenv('HOST_REDIS')

PORT_REDIS = os.getenv('PORT_REDIS')
