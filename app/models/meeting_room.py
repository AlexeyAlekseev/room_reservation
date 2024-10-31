from sqlalchemy import Column, String, Text

from app.core.db import Base, PreBase


class MeetingRoom(Base, PreBase):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)