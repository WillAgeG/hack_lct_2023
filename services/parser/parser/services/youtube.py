import logging

import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials

from ..core.configs import API_SERVICE_NAME, API_VERSION, CLIENT_ID, CLIENT_SECRET, SCOPES


logging.basicConfig(
    filename='main.log',
    filemode='w',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)


class YoutubeAPIParser:
    """
    Предоставялет данные пользователя по YouTube API.
    """
    def __init__(
        self,
        access_token: str,
        refresh_token: str
    ) -> None:
        user_info = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'access_token': access_token,
            'refresh_token': refresh_token,
            'token_uri': 'https://oauth2.googleapis.com/token'
        }

        credentials = Credentials.from_authorized_user_info(
            info=user_info,
            scopes=SCOPES
        )

        self.youtube = googleapiclient.discovery.build(
            API_SERVICE_NAME,
            API_VERSION,
            credentials=credentials
        )
        self.channel_id = self. __get_channel_id()

    def __get_channel_id(self):
        channels_response = self.youtube.channels().list(
            part='id',
            mine=True
        ).execute()

        channel_id = channels_response['items'][0]['id']

        return channel_id

    def get_data(self):
        data = {
            "liked_videos": self.get_channel_stats(),
            # ...
        }
        return data

    def get_channel_stats(self):
        request = self.youtube.channels().list(
            part='snippet,contentDetails,statistics',
            id=self.channel_id
        )
        response = request.execute()

        data = dict(
            Channel_name=response['items'][0]['snippet']['title'],
            Subscribers=response['items'][0]['statistics']['subscriberCount'],
            Description=response['items'][0]['snippet']['description'],
            Views=response['items'][0]['statistics']['viewCount'],
            Total_videos=response['items'][0]['statistics']['videoCount']
        )

        return data
