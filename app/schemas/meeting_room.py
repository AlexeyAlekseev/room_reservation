from typing import Optional

from pydantic import BaseModel, Field


class MeetingRoomCreate(BaseModel):
    name: str = Field(..., max_length=100, nullable=False)
    description: Optional[str]