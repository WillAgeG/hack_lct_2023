import logging

from fastapi import FastAPI, Response
from fastapi.openapi.docs import get_swagger_ui_html

from .models.predictions import Predict
from .services.predictions import create_prediction

app = FastAPI()

logging.basicConfig(
    filename='general.log',
    filemode='w',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)


@app.post('/api/v1/predictor/')
async def start_predicting(
    predict: Predict,
    response: Response
):
    try:
        await create_prediction(
            predict.auth_token,
            predict.predict_id
        )

        response.status_code = 200
        return {
            'message': 'Predicting started'
        }

    except Exception as e:
        response.status_code = 500
        logger.error('Predicting error %s', e)
        return {
            'message': 'Predicting error'
        }


@app.get('/api/v1/predictor/doc', include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url='/api/v1/predictor/openapi.json',
        title='Custom Swagger UI'
    )


@app.get('/api/v1/predictor/openapi.json', include_in_schema=False)
async def get_openapi():
    return app.openapi()
