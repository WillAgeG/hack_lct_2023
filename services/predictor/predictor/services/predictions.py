import logging
import re

import isodate
import numpy as np
import pandas as pd
import requests
from catboost import CatBoostClassifier
from requests import Response
from sklearn.feature_extraction.text import CountVectorizer

logger = logging.getLogger(__name__)


def insert_prediction(
    predict_id: str | int,
    predict: dict,
    auth_token: str
) -> Response:
    """
    Отправить запрос создание предсказания.
    """
    accounts_domain = 'http://accounts:8000'
    url = f'{accounts_domain}/api/v1/accounts/insert_predictions/{predict_id}/'
    data = {
        'predict': predict
    }

    response = requests.patch(
        url,
        json=data,
        headers={
            'Authorization': ('Token ' + auth_token)
        }
    )

    if response.status_code != 200:
        logger.error(
            'Request failed with status code: %s. Response data: %s',
            response.status_code,
            response.json()
        )

    return response


def get_youtube_data(
    auth_token: str
) -> Response:
    """
    Получить спаршенные данные с youtube.
    """
    url = 'http://parser:8000/api/v1/parser/'
    data = {
        'auth_token': auth_token
    }

    response = requests.post(
        url,
        json=data
    )

    if response.status_code != 200:
        error_msg = (
            'Request failed with status code: %s. Response data: %s',
            response.status_code,
            response.json()
        )
        logger.error(error_msg)
        raise ValueError(error_msg)

    return response.json()


def get_prediction_from_ai(youtube_data: dict) -> dict[dict, dict, dict]:
    """Получить спрогнозированные данные."""

    my_liked_videos_stats = youtube_data
    my_liked_videos_data = pd.DataFrame(my_liked_videos_stats)

    video_categories_weights = pd.read_excel('video_categories.xlsx')

    video_categories_weights['Id_video_category'] = video_categories_weights['Id_video_category'].astype(int)
    my_liked_videos_data['Id_video_category'] = my_liked_videos_data['Id_video_category'].astype(int)
    df = my_liked_videos_data.merge(
        video_categories_weights,
        left_on='Id_video_category',
        right_on="Id_video_category"
    )

    df['total_seconds'] = df['Duration'].apply(isodate.parse_duration)

    interval_min = np.timedelta64(1, 'm')
    interval_max = np.timedelta64(200, 'm')
    filtered_dataset = df[(df['total_seconds'] > interval_min) & (df['total_seconds'] < interval_max)]

    filtered_dataset.loc[:, 'Title'] = filtered_dataset.loc[:, 'Title'].str.lower()
    filtered_dataset.loc[:, 'Title'] = filtered_dataset.loc[:, 'Title'].str.replace('\d+', '', regex=True)
    filtered_dataset.loc[:, 'Title'] = filtered_dataset.loc[:, 'Title'].str.replace('[^а-яА-Яa-zA-Z\s]', '', regex=True)

    df_c = filtered_dataset[['Category', 'LikeCount']].groupby(['Category']).count().sort_values(by='LikeCount', ascending=False).reset_index()
    df_c = df_c.head(10)

    df_c = df_c.to_json(orient='records')
    result = df_c
    result = result.encode('utf-8').decode('unicode_escape')

    res = [item for sublist in filtered_dataset['Tags'] if sublist is not None for item in sublist]

    res = [x.lower() for x in res]
    res = [re.sub('\d+', '', x) for x in res]
    res = [re.sub('[^а-яА-Яa-zA-Z\s]', '', x) for x in res]
    res = [x.strip() for x in res]
    res = [x for x in res if x.strip() != '']

    tag_counts = {}
    for tag in res:
        tag_counts[tag] = tag_counts.get(tag, 0) + 1

    sorted_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)
    top_tags = sorted_tags[:50]

    result2 = pd.DataFrame(top_tags, columns=['Title', 'Count'])
    result2 = result2.to_json(orient='records')
    result2 = result2.encode('utf-8').decode('unicode_escape')

    # Использование реальных данных
    model = CatBoostClassifier()
    model.load_model('catboost_model.bin')

    df = pd.DataFrame(res)
    df = df.rename(columns={0: 'Tag'})
    df['Tag'] = df['Tag'].astype(str)

    text_array = df['Tag'].values.astype(str)
    arr_obj = text_array.astype(object)

    vectorizer = CountVectorizer()
    X_train_bow = vectorizer.fit_transform(arr_obj)

    predictions = model.predict(X_train_bow)

    result3 = pd.DataFrame(predictions)
    result3 = result3.rename(columns={0: 'Tag'})
    result3 = result3.groupby(by='Tag').size()
    result3 = result3.reset_index()
    result3 = result3.to_json(orient='records')
    result3 = result3.encode('utf-8').decode('unicode_escape')

    return {
        'result': result,
        'result2': result2,
        'result3': result3,
    }


async def create_prediction(
    auth_token: str,
    predict_id: str
) -> None:
    """
    Таск селери создание предсказания.

    Предсказание будет создано и через accounts сервис передано в бд.
    """
    youtube_data = get_youtube_data(
        auth_token
    )
    prediction_data = get_prediction_from_ai(youtube_data)
    insert_prediction(
        predict_id,
        prediction_data,
        auth_token
    )
