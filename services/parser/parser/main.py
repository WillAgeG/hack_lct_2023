import logging
from typing import Annotated

from fastapi import Body, FastAPI, Response
from fastapi.openapi.docs import get_swagger_ui_html

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


@app.post('/api/v1/parser/')
async def parse_data(
    user_data: UserData,
    response: Response
):
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


@app.get('/api/v1/parser/doc', include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url='/api/v1/parser/openapi.json',
        title='Custom Swagger UI'
    )


@app.get('/api/v1/parser/openapi.json', include_in_schema=False)
async def get_openapi():
    return app.openapi()
