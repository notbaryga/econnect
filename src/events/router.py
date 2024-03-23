from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.data.database import get_async_session
from src.events.models import EventTable
from src.events.schemas import EventAdd


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
async def get_events(session: AsyncSession = Depends(get_async_session)):
    query = select(EventTable)
    result = await session.execute(query)
    return result.mappings().all()


@router.post("/add_event/")
async def add_event(new_event: EventAdd = Depends(), session: AsyncSession = Depends(get_async_session)):
    stmt = insert(EventTable).values(**new_event.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/delete_event/")
async def delete_event(id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(EventTable).where(EventTable.c.id == id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
