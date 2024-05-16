import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from typing import List
from domain.models.product_model import ProductModel
from domain.repositories.product_repository import ProductRepository

class ProductUseCase:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def create(self, product: ProductModel) -> ProductModel:
        return self.product_repository.create(product)

    def get_all(self) -> List[ProductModel]:
        return self.product_repository.get_all()

    def eliminate(self, product_id: int) -> None:
        self.product_repository.eliminate(product_id)