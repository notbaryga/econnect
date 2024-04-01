from sqlalchemy import Table, Column, Integer, String, DateTime
from data.database import metadata

EventTable = Table(
    "Events",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("name", String),
    Column("description", String),
    Column("datetime", DateTime),
    Column("location", String),
    Column("type", String),
    Column("photo", String),
    Column("reward", Integer)
)
