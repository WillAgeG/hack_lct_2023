from pydantic import BaseModel


class Predict(BaseModel):
    predict_id: str
    auth_token: str
