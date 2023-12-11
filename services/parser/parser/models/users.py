from pydantic import BaseModel


class UserData(BaseModel):
    access_token: str
    refresh_token: str
