from sqlalchemy import *
from sqlalchemy import exc as sa_exc
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import warnings

from config import BASE_CONFIG
from database.db_mods.db_mods import *
from database.db_history.db_history import *
from database.db_operation.db_operation import *
from database.base import base


warnings.filterwarnings('ignore', category=sa_exc.SAWarning)


timeout = 10
engine = create_engine(f'mysql+pymysql://{BASE_CONFIG["BASE_USER"]}:{BASE_CONFIG["BASE_PASSWORD"]}@{BASE_CONFIG["BASE_HOST"]}/{BASE_CONFIG["BASE_TABLE"]}', connect_args={'connect_timeout': timeout})


base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()