from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from data.database import get_async_session

from points.models import PointTable
from points.schemas import PointAdd


router = APIRouter(
    prefix='/points',
    tags= ['Points']
)

@router.get("/{id}")
async def get_point_by_id(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(PointTable).where(PointTable.c.id == id)
    result = await session.execute(query)
    return result.mappings().all()

@router.get("/")
async def get_points(session: AsyncSession = Depends(get_async_session)):
    query = select(PointTable)
    result = await session.execute(query)
    return result.mappings().all()


@router.post("/add_point/")
async def add_point(new_point: PointAdd = Depends(), session: AsyncSession = Depends(get_async_session)):
    stmt = insert(PointTable).values(**new_point.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/delete_point/")
async def delete_point(id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(PointTable).where(PointTable.c.id == id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
