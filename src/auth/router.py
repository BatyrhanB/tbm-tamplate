import json
from bson import json_util

from fastapi import APIRouter, HTTPException
from pymongo.errors import PyMongoError

from src.settings.mongo_db import codes_collection

auth_router = APIRouter(prefix="", tags=["auth"])


@auth_router.get("/all_codes")
async def get_all_codes():
    all_codes = codes_collection.find()
    data = []
    async for code in all_codes:
        data.append(json.loads(json_util.dumps(code)))

    response = json.loads(json_util.dumps(data))
    return response


@auth_router.delete("/delete_all_codes")
async def delete_all_codes():
    try:
        result = codes_collection.delete_many({})

        if result.deleted_count > 0:
            return {"message": f"Successfully deleted {result.deleted_count} codes."}
        else:
            return {"message": "No codes found to delete."}

    except PyMongoError:
        raise HTTPException(
            status_code=500, detail="An error occurred while deleting codes."
        )
