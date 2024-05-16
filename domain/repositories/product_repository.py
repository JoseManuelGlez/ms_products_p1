import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from typing import List
from abc import ABC, abstractmethod
from domain.models.product_model import ProductModel

class ProductRepository(ABC):
    @abstractmethod
    def create(self, product: ProductModel) -> ProductModel:
        pass

    @abstractmethod
    def get_all(self) -> List[ProductModel]:
        pass

    @abstractmethod
    def eliminate(self, product_id: int) -> None:
        pass