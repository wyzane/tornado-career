from config.db import model


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
