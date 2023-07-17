import uuid
from typing import Union

from fastapi import Depends
from fastapi_users import BaseUserManager, UUIDIDMixin, InvalidPasswordException

from src.settings.config import settings
from src.auth.models import User
from src.auth.schemas import UserCreate
from src.settings.database import get_user_db



class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = settings.SECRET_KEY
    verification_token_secret = settings.SECRET_KEY

    async def validate_password(
        self,
        password: str,
        user: Union[UserCreate, User],
    ) -> None:
        if len(password) < 8:
            raise InvalidPasswordException(
                reason="Password should be at least 8 characters"
            )
        if user.email in password:
            raise InvalidPasswordException(
                reason="Password should not contain e-mail"
            )

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)