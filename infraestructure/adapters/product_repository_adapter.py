import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from typing import List
from flask import jsonify
from domain.models.product_model import ProductModel
from domain.repositories.product_repository import ProductRepository
from infraestructure.adapters.data_sources.entities.product_entity import ProductEntity
from infraestructure.adapters.data_sources.db_config import db

class ProductRepositoryAdapter(ProductRepository):
    def create(self, product: ProductModel):
        new_product = ProductEntity(name=product.name, price=product.price, stock=product.stock)
        db.add(new_product)
        db.commit()
        db.refresh(new_product)

        product_dict = {
        'id': new_product.id,
        'name': new_product.name,
        'price': new_product.price,
        'stock': new_product.stock
    }
        return jsonify(product_dict), 201

    def get_all(self) -> List[ProductModel]:
        return db.query(ProductEntity).all()

    def eliminate(self, product_id: str) -> None:
        db.query(ProductEntity).filter(ProductEntity.id == product_id).delete()
        db.commit()