from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.meeting_room import MeetingRoom
from app.schemas.meeting_room import MeetingRoomCreate


async def create_meeting_room(
        new_room: MeetingRoomCreate,
        session: AsyncSession,
) -> MeetingRoom:
    new_room_data = new_room.dict()
    db_room = MeetingRoom(**new_room_data)
    session.add(db_room)
    await session.commit()
    await session.refresh(db_room)
    return db_room

async def get_room_id_by_name(
        room_name: str,
        session: AsyncSession,
) -> Optional[int]:
    db_room_id =await session.execute(
        select(MeetingRoom.id).where(MeetingRoom.name == room_name)
    )
    db_room_id = db_room_id.scalars().first()
    return db_room_id

async def read_all_rooms_from_db(
        session: AsyncSession,
) -> list[MeetingRoom]:
    db_rooms = await session.execute(select(MeetingRoom))
    db_rooms_name = db_rooms.scalars().all()
    return db_rooms_name


async def get_meeting_room_by_id(
        room_id: int,
        session: AsyncSession,
) -> Optional[MeetingRoom]:
    db_room = await session.execute(
        select(MeetingRoom).where(MeetingRoom.id == room_id)
    )
    db_room = db_room.scalars().first()
    return db_room