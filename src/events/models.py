from datetime import UTC
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey
from data.database import metadata

EventTable = Table(
    "Event",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String),
    Column("description", String),
    Column("datetime", TIMESTAMP, default=UTC),
    Column("location", String),
    Column("type", String),
    Column("photo", String),
    Column("reward", Integer),
    Column("creator_id", ForeignKey("user.id", ondelete="CASCADE"))
)
