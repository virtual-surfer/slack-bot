import os
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
MYSQL_HOST = os.environ['MYSQL_HOST']
MYSQL_DB = os.environ['MYSQL_DB']

engine = create_engine('mysql://{user}:{password}@{host}/{db}'
                       .format(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOST, db=MYSQL_DB),
                       encoding='utf-8', echo=False)
metadata = MetaData(engine)
Base = declarative_base()


class TwitterUser(Base):
    __tablename__ = 'twitter_user'

    twitter_user_id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    user_screen_name = Column(String, nullable=False)
    profile_image_link = Column(String, nullable=False)
    ins_datetime = Column(DATETIME, default=datetime.now, nullable=False)
    upd_datetime = Column(DATETIME, default=datetime.now, nullable=False)


if __name__ == "__main__":
    # create table
    Base.metadata.create_all(engine)