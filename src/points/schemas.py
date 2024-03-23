from pydantic import BaseModel, ConfigDict
from typing import Optional
from enum import Enum


class PointType(Enum):
    shit = 'Грязь и мусор'
    tires = 'Свалка шин'
    dumpsters = 'Переполненные контейнеры'
    petrol = 'Разлив нефти'
    blawn = 'Парковка на газонах'
    commerce = 'Несанкционированная торговля'
    improvement = 'Нарушение благоустройства'


class StatusType(Enum):
    not_watched = 'Не просмотрено'
    process = 'В процессе'
    done = 'Решено'


class PointAdd(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    type: PointType
    photo: Optional[str] = None
    reward: Optional[int] = None
    status: StatusType
    creator_id: int

    class Config:
        use_enum_values = True


class Point(PointAdd):
    id: int
    model_config = ConfigDict(from_attributes=True, use_enum_values=True)