from sqlalchemy import Column, DateTime, Integer, ForeignKey

from app.core.db import Base, PreBase


class Reservation(Base, PreBase):
    from_reserve = Column(DateTime)
    to_reserve = Column(DateTime)
    meetingroom_id = Column(Integer, ForeignKey('meetingroom.id'))

    def __repr__(self):
        return (
            f'Уже забронировано с {self.from_reserve} по {self.to_reserve}'
        )
