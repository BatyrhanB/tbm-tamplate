from datetime import datetime

from pydantic import BaseModel


class ProductCreate(BaseModel):
    id: int
    title : str
    description : str
    category_id: int 
    type : str
    origin : str
    certification : str
    color: str
    price : float
    created_at: datetime