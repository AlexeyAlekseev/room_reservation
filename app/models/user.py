from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from app.core.db import Base, PreBase


class User(SQLAlchemyBaseUserTable[int], Base, PreBase):
    pass
