from db.base import Base
from db.session import engine
from db.models import *


def create_tables():
    Base.metadata.create_all(bind=engine)


create_tables()
