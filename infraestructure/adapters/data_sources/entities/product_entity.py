import os
import sys
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from sqlalchemy import Column, Integer, String, Float
from infraestructure.adapters.data_sources.db_config import Base, engine

class ProductEntity(Base):
    __tablename__ = 'products'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
    name = Column(String(255))
    price = Column(Float)
    stock = Column(Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock
        }

Base.metadata.create_all(bind=engine)