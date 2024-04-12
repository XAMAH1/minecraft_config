from sqlalchemy.orm import relationship

from database.base import base
from sqlalchemy import *


class history(base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    mod_name = Column(String(255), nullable=False)
    datetime = Column(DATETIME, nullable=False)
    operation = Column(Integer, ForeignKey('operation.id'))
    operation_realt = relationship("operation")
