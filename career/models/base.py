# from sqlalchemy import Table, MetaData
# from sqlalchemy.ext.declarative import declarative_base
#
# from config.db import engine_db_career
#
#
# Base = declarative_base()
#
#
# def model(table):
#     class BaseModel(Base):
#         __tablename__ = table
#         metadata = MetaData(engine_db_career)
#
#         # 映射数据库中同名的表
#         Table(__tablename__, metadata, autoload=True)
#
#     return BaseModel