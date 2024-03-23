from fastapi import FastAPI

from src.events.router import router as events_router
from src.points.router import router as points_router


app = FastAPI(
    title="Econnect"
)

app.include_router(events_router)

app.include_router(points_router)

@app.get('/')
def start():
    return {"status": "success"}