from sqlalchemy import (
    Column, text,
    SmallInteger, Integer,
    Float, String, TIMESTAMP
)

from ..database import db


class ApartmentPrice(db.Model):
    __tablename__ = 'apartment_price'
    __table_args__ = {'schema': 'wonder'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    summary = Column(String(512), nullable=False, comment='brief description')
    price = Column(Integer, nullable=False, comment='[rate = 100] Real price = price / rate(100)')
    area = Column(Float, nullable=False)
    decoration = Column(SmallInteger, nullable=False, default=0, comment='0:unknow 1:blank 2:paperback 3:hardback 4:luxury')
    layout = Column(SmallInteger, nullable=False, default=0, comment='0:unknow 1:南北 2:两南 3:两北')
    rooms = Column(SmallInteger, nullable=False, default=1, comment='room number of apartment')
    region = Column(String(128), nullable=True, comment='location name, like "七宝 陆家嘴 张江"')
    detail_url = Column(String(512), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))