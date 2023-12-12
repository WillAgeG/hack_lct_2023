import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# Youtube
API_SERVICE_NAME = 'youtube'

API_VERSION = 'v3'

CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')

CLIENT_SECRET = os.getenv('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')

CLEINT_JSON_SECRET = {
    "web": {
        "client_id": CLIENT_ID,
        "project_id": "compass-407606",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": CLIENT_SECRET,
        "redirect_uris": ["http://127.0.0.1:9000/"]
    }
}

SCOPES = [
    "https://www.googleapis.com/auth/youtube.readonly",
]

# Accounts service
ACCOUNTS_HOST = 'https://compas.fun'
