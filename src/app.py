from fastapi import FastAPI
from fastapi_users import FastAPIUsers


from events.router import router as events_router
from points.router import router as points_router

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate


app = FastAPI(
    title="Econnect"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(events_router)
app.include_router(points_router)


@app.get('/')
def start():
    return {"status": "success"}