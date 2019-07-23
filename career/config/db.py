"""数据库配置，包括数据库engine、session等
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


db_career = {
    "user": "postgres",
    "pass": "wyzane",
    "host": "127.0.0.1",
    "port": "5432",
    "db": "career_tornado"
}


engine_db_career = create_engine(
    "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
        db_career["user"],
        db_career["pass"],
        db_career["host"],
        db_career["port"],
        db_career["db"]
    ),
    encoding="utf-8",
    # echo=True
)

db_career = scoped_session(
    sessionmaker(
        bind=engine_db_career,
        autocommit=False,
        autoflush=True,
        expire_on_commit=False
    )
)
