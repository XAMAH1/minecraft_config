from sqlalchemy.orm import relationship

from database.base import base
from sqlalchemy import *


class mods(base):
    __tablename__ = 'mods'

    id = Column(Integer, primary_key=True)
    mod_name = Column(String(255), nullable=False)
    path_mod = Column(String(255), nullable=False)
    datetime = Column(DATETIME, nullable=False)
