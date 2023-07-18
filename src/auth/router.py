from fastapi import APIRouter, Request, Body

from src.auth.security import verifyEmail


auth_router = APIRouter(prefix="", tags=["auth"])


@auth_router.post("/confirmation/")
async def confirmation(
    request: Request,
    token: str = Body(..., embed=True),
):
    result = await verifyEmail(token)
    if result:
        return {"message": "Email is confirmed"}
    return {"message": "Email not confirmed"}
