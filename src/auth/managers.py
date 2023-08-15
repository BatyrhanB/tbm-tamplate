import uuid
from typing import Union, Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin, InvalidPasswordException

from src.settings.config import settings
from src.auth.models import User
from src.auth.schemas import UserCreate, UserDB
from src.settings.database import get_user_db
from src.auth.utils import send_email_async, generate_otp
from src.auth.helper import add_otp_code


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
            raise InvalidPasswordException(reason="Password should not contain e-mail")

    async def on_after_register(self, user: UserDB, request: Optional[Request] = None):
        code = await generate_otp()
        otp_data = {"email": user.email, "code": code}
        saved_otp = await add_otp_code(otp_data)
        if saved_otp:
            await send_email_async("Email Confirmation", user.email)
        else:
            print("Failed to save OTP data to the database.")

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
