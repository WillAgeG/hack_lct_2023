import logging

from fastapi import FastAPI, Response

from .models.users import UserData
from .services.youtube import YoutubeAPIParser

app = FastAPI()


logging.basicConfig(
    filename='main.log',
    filemode='w',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)


@app.get('/api/v1/parser/')
async def parse_data(user_data: UserData, response: Response):
    youtube_parser = YoutubeAPIParser(
        user_data.access_token,
        user_data.refresh_token
    )

    try:
        data = youtube_parser.get_data()
        response.status_code = 200
        return data

    except Exception as e:
        logger.error(e)
        response.status_code = 500
        return {
            'message': 'Something went wrong'
        }
