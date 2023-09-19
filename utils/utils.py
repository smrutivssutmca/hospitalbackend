from datetime import datetime, timedelta
import jwt
from django.conf import settings


def create_access_token(username, id, expire_time):
    encode = {"username": username, "id": id}

    if expire_time:
        expire = datetime.utcnow() + timedelta(minutes=expire_time)
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    encode.update({"exp": expire})

    return jwt.encode(encode, settings.SECRET_KEY, "HS256"), expire
