from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from src.settings.base_model import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"
    pass
