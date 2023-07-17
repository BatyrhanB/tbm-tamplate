import uuid

from pydantic import BaseModel

class BaseSchema(BaseModel):
    id : uuid.UUID