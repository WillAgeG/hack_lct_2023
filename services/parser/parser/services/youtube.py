import logging

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from ..core.configs import (API_SERVICE_NAME, API_VERSION)

logger = logging.getLogger(__name__)


class YoutubeAPIParser:
    """
    Предоставялет данные пользователя по YouTube API.
    """
    def __init__(self, access_token: str) -> None:
        credentials = Credentials(access_token)

        self.youtube = googleapiclient.discovery.build(
            API_SERVICE_NAME, API_VERSION, credentials=credentials
        )

    def get_youtube_data(self) -> list[dict]:
        """Парсинг данных youtube"""
        all_data = []
        nextPageToken = None
        for i in range(1, 40):  # 40 Потому что больше 2000 данных будет избыточно.
            request = self.youtube.videos().list(
                part="snippet,contentDetails,statistics,player",
                myRating="like",
                maxResults=50,
                pageToken=nextPageToken
            )

            response = request.execute()

            for i in range(len(response['items'])):
                data = dict(
                    PublishedAt=response['items'][i]['snippet']['publishedAt'],
                    ChannelId=response['items'][i]['snippet']['channelId'],
                    Title=response['items'][i]['snippet']['title'],
                    Tags=response['items'][i]['snippet'].get('tags'),
                    Kind=response['items'][i]['kind'],
                    Description=response['items'][i]['snippet']['description'],
                    ChannelTitle=response['items'][i]['snippet']['channelTitle'],
                    Id_video_category=response['items'][i]['snippet']['categoryId'],
                    liveBroadcastContent=response['items'][i]['snippet']['liveBroadcastContent'],
                    Duration=response['items'][i]['contentDetails']['duration'],
                    ViewCount=response['items'][i]['statistics'].get('viewCount'),
                    LikeCount=response['items'][i]['statistics'].get('likeCount'),
                )
                all_data.append(data)

            nextPageToken = response.get('nextPageToken')
            if not nextPageToken:
                break

        return all_data
