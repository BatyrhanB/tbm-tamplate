import uvicorn

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.settings.config import settings
from src.product.router import router as product_router

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

app.include_router(
    product_router,
    prefix="/api/v1",
    tags=["product"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)