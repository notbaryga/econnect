from sqlalchemy import Table, Column, Integer, String, ForeignKey
from data.database import metadata

PointTable = Table(
    "Point",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String),
    Column("description", String),
    Column("location", String),
    Column("type", String),
    Column("photo", String),
    Column("reward", Integer),
    Column("status", String),
    Column("creator_id", ForeignKey("user.id", ondelete="CASCADE"))
)
