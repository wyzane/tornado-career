from sqlalchemy import Column, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class DeletedModel(Base):

    __abstract__ = True

    is_deleted = Column(Boolean, nullable=False, default=False)


class TimeModel(Base):

    __abstract__ = True

    pass