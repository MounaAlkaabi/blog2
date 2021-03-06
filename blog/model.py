import datetime

from sqlalchemy import Column, Integer, String, \
    Sequence, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, engine

from flask.ext.login import UserMixin

class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True)
    title = Column(String(1024))
    content = Column(Text)
    datetime = Column(DateTime, default=datetime.datetime.now)

Base.metadata.create_all(engine)