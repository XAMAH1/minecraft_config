from sqlalchemy.orm import relationship

from database.base import base
from sqlalchemy import *


class operation(base):
    __tablename__ = 'operation'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
