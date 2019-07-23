from sqlalchemy import Table, MetaData
from sqlalchemy.ext.declarative import declarative_base

from config.db import engine_db_career


Base = declarative_base()


def model(table):
    class BaseModel(Base):
        __tablename__ = table
        metadata = MetaData(engine_db_career)

        # 映射数据库中同名的表
        Table(__tablename__, metadata, autoload=True)

    return BaseModel


TB_CAREER_HOBBY = model("career_hobby")


# class Hobby(Base):
#
#     __tablename__ = "career_hobby"
#
#     id = Column(Integer, primary_key=True,
#                 autoincrement=True, nullable=False)
#     desc = Column(String(1024), nullable=False)
#     created = Column(DateTime, nullable=False)
#     modified = Column(DateTime, nullable=False)
#     operator = Column(String(64))
