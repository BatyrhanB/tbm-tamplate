import secrets
from decouple import config
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, PostgresDsn, validator


class Settings(BaseSettings):
    API_VERSION: str = "v1"
    API_V1_STR: str = f"/api/{API_VERSION}"
    PROJECT_NAME: str = "Marketplace Fast API"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 1  # 1 hour
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 100  # 100 days
    SERVER_HOST: AnyHttpUrl = config("SERVER_HOST")
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = config("CORS_ORIGINS")

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = "Marketplace"

    POSTGRES_SERVER: str = config("POSTGRES_SERVER")
    POSTGRES_USER: str = config("POSTGRES_USER")
    POSTGRES_PASSWORD: str = config("POSTGRES_PASSWORD")
    POSTGRES_DB: str = config("POSTGRES_DB")
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = "postgresql+asyncpg://postgres:postgres@marketplace_db:5432/postgres" 

    #@validator("SQLALCHEMY_DATABASE_URI", pre=True)
    #def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
    #    if isinstance(v, str):
    #        return v
    #    return PostgresDsn.build(
    #        scheme="postgresql+asyncpg",
    #        user=values.get("POSTGRES_USER"),
    #        password=values.get("POSTGRES_PASSWORD"),
    #        host=values.get("POSTGRES_SERVER"),
    #        path=f"/{values.get('POSTGRES_DB') or ''}",
    #    )

    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = 587
    SMTP_HOST: Optional[str] = "smtp.gmail.com"
    SMTP_USER: Optional[str] = config("SMTP_USER")
    SMTP_PASSWORD: Optional[str] = config("SMTP_PASSWORD")
    EMAILS_FROM_EMAIL: Optional[EmailStr] = config("EMAILS_FROM_EMAIL")
    EMAILS_FROM_NAME: Optional[str] = "SaleHub"

    @validator("EMAILS_FROM_NAME")
    def get_project_name(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if not v:
            return values["PROJECT_NAME"]
        return v

    EMAILS_ENABLED: bool = True

    @validator("EMAILS_ENABLED", pre=True)
    def get_emails_enabled(cls, v: bool, values: Dict[str, Any]) -> bool:
        return bool(
            values.get("SMTP_HOST")
            and values.get("SMTP_PORT")
            and values.get("EMAILS_FROM_EMAIL")
        )

    FIRST_SUPERUSER: EmailStr = config("FIRST_SUPERUSER")
    FIRST_SUPERUSER_PASSWORD: str = config("FIRST_SUPERUSER_PASSWORD")

    class Config:
        case_sensitive = True


settings = Settings()
