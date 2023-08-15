import secrets
from pathlib import Path
from fastapi_mail import MessageSchema, FastMail, ConnectionConfig

from src.settings.config import settings
from src.auth.helper import add_otp_code


BASE_DIR = Path(__file__).resolve().parent.parent

conf = ConnectionConfig(
    MAIL_USERNAME=settings.SMTP_USER,
    MAIL_PASSWORD=settings.SMTP_PASSWORD,
    MAIL_FROM=settings.EMAILS_FROM_EMAIL,
    MAIL_PORT=settings.SMTP_PORT,
    MAIL_SERVER=settings.SMTP_HOST,
    MAIL_FROM_NAME=settings.EMAILS_FROM_NAME,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    TEMPLATE_FOLDER=Path(BASE_DIR, "templates"),
)


async def generate_otp(length=6):
    """Asynchronous function to generate an OTP code of the specified length."""
    if length < 1:
        raise ValueError("OTP length must be at least 1")

    return "".join(secrets.choice("0123456789") for _ in range(length))


async def send_email_async(subject: str, email_to: str):
    code = await generate_otp()
    await add_otp_code(otp_data={"email": email_to, "code": code})
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=code,
        subtype="html",
    )
    fm = FastMail(conf)
    await fm.send_message(message, template_name="email.html")
