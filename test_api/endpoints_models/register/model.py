from faker import Faker
from pydantic import BaseModel
from pydantic.class_validators import Dict, Optional

fake = Faker()


class Data(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class Support(BaseModel):
    url: str
    text: str


class ResponseReqres(BaseModel):
    """Модель для ответа."""

    data: Data
    support: Support
