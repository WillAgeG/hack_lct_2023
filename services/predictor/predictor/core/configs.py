import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# Domain
DOMAIN = os.getenv('DOMAIN')

PREFIX_DOMAIN = os.getenv('PREFIX_DOMAIN')
