from sqlalchemy import Column, Integer, String

from src import Base


class MathTask(Base):
    __tablename__ = "task"

    id = Column("id", Integer, primary_key=True, index=True)
    category = Column("category", String)
    topic = Column("topic", String)
    difficulty = Column("difficulty", Integer)


