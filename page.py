from sqlalchemy import Column, Integer, String, Boolean, Float
from connection import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Page(Base):
    __tablename__ = 'page'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    descr = Column(String)
    ads = Column(String)
    ssl = Column(Boolean)
    points = Column(Float)
    multilang = Column(String)

    origin = Column(String, ForeignKey('website.domain'))
    website = relationship('Website', backref='pages')
