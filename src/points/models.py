from sqlalchemy import Table, Column, Integer, String, MetaData


metadata = MetaData()

PointTable = Table(
    "Points",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("name", String),
    Column("description", String),
    Column("location", String),
    Column("type", String),
    Column("photo", String),
    Column("reward", Integer),
    Column("status", String),
    Column("creator_id", Integer),
)
