import uuid
import uvicorn

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.settings.config import settings
from src.product.router import router as product_router
from src.product.router import category_router

from fastapi_users import FastAPIUsers
from src.auth.managers import get_user_manager
from src.auth.security import auth_backend
from src.auth.models import User
from src.auth.schemas import UserCreate, UserRead, UserUpdate
from src.auth.router import auth_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)


if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

app.include_router(auth_router, prefix="/auth", tags=["auth"])

app.include_router(
    product_router,
    prefix="/api/v1",
    tags=["product"],
)

app.include_router(
    category_router,
    prefix="/api/v1",
    tags=["category"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
