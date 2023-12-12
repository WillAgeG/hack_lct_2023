from pydantic import BaseModel


class UserData(BaseModel):
    auth_token: str
