from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from data.database import get_async_session

from points.models import PointTable
from points.schemas import PointAdd, PointType, StatusType

from auth.models import User
from auth.base_config import current_user

router = APIRouter(
    prefix='/points',
    tags=['Points']
)


@router.get("/{id}")
async def get_point_by_id(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(PointTable).where(PointTable.c.id == id)
    result = await session.execute(query)
    return result.mappings().all()


@router.get("/")
async def get_points(session: AsyncSession = Depends(get_async_session), point_type: PointType = None,
                     status_type: StatusType = None, creator_id: int = None):
    query = select(PointTable)

    if point_type:
        query = query.where(PointTable.c.type == point_type.value)

    if status_type:
        query = query.where(PointTable.c.status == status_type.value)

    if creator_id:
        query = query.where(PointTable.c.creator_id == creator_id)

    result = await session.execute(query)
    return result.mappings().all()


@router.get("/my/")
async def get_my_points(session: AsyncSession = Depends(get_async_session), user: User = Depends(current_user)):
    query = select(PointTable).where(PointTable.c.creator_id == user.id)
    result = await session.execute(query)
    return result.mappings().all()


@router.post("/add_point/")
async def add_point(new_point: PointAdd = Depends(), session: AsyncSession = Depends(get_async_session),
                    user: User = Depends(current_user)):
    point = new_point.dict()['creator_id'] = user.id
    stmt = insert(PointTable).values(**point)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/delete_point/")
async def delete_point(id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(PointTable).where(PointTable.c.id == id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
