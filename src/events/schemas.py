from enum import Enum
from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class EventType(Enum):
    swap = 'Своп'
    cleaning_day = 'Субботник'
    lecture = 'Лекция'
    festivales = 'Фестивали'
    master_classes = 'Мастер-классы'
    kvesti = 'Квесты'
    actions = 'Экологические акции'
    other = 'Другое'

class EventAdd(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    datetime: Optional[datetime] = None
    location: Optional[str] = None
    type: EventType
    photo: Optional[str] = None
    reward: Optional[int] = None

    class Config:
        use_enum_values = True

class Event(EventAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)