from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime


metadata = MetaData()

EventTable = Table(
    "events",
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
