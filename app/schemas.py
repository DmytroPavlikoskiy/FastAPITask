from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str
    role: str = "user"


class LoginUsers(BaseModel):
    username: str
    password: str


class MessageRequest(BaseModel):
    bot_token: str
    chat_id: str
    message: str