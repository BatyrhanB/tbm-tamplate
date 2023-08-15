from bson.objectid import ObjectId
from motor import motor_asyncio

from src.settings.config import settings


client = motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URL)

database = client.codes

codes_collection = database.get_collection("codes_collection")

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")