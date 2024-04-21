from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import User
from auth.base_config import current_user

from data.database import get_async_session
from events.models import EventTable
from events.schemas import EventAdd, EventType


router = APIRouter(
    prefix='/events',
    tags= ['Events']
)

@router.get("/{id}")
async def get_event_by_id(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(EventTable).where(EventTable.c.id == id)
    result = await session.execute(query)
    return result.mappings().all()

@router.get("/")
async def get_events(session: AsyncSession = Depends(get_async_session), type: EventType = None, creator_id: int = None):
    query = select(EventTable)

    if type:
        query = query.where(EventTable.c.type == type.value)

    if creator_id:
        query = query.where(EventTable.c.creator_id == creator_id)

    result = await session.execute(query)
    return result.mappings().all()

@router.get("/my/")
async def get_my_events(session: AsyncSession = Depends(get_async_session), user: User = Depends(current_user)):
    query = select(EventTable).where(EventTable.c.creator_id == user.id)
    result = await session.execute(query)
    return result.mappings().all()


@router.post("/add_event/")
async def add_event(new_event: EventAdd = Depends(), session: AsyncSession = Depends(get_async_session), user: User = Depends(current_user)):
    event = new_event.dict()['creator_id'] = user.id
    stmt = insert(EventTable).values(**event)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/delete_event/")
async def delete_event(id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(EventTable).where(EventTable.c.id == id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
