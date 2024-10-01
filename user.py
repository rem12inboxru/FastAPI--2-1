from app.backend.db import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models import *
class User(Base):
    __tablename__ = "users"
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True )
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    tasks = relationship('Task', back_populates='user')

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))