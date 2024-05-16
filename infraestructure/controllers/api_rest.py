import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

sys.path.insert(0, r'C:\Users\12345\Desktop\ms-products')

from flask import Flask, request, jsonify
from infraestructure.adapters.product_repository_adapter import ProductRepositoryAdapter
from domain.models.product_model import ProductModel
from domain.uses_cases.product_use_case import ProductUseCase

app = Flask(__name__)

product_repository = ProductRepositoryAdapter()
product_use_case = ProductUseCase(product_repository)

class ApiRest:
    @app.route('/products', methods=['POST'])
    def create_product():
        data: dict = request.get_json()
        estudiante = ProductModel(name=data['name'], price=data['price'], stock=data['stock'])
        return product_use_case.create(estudiante)

    @app.route('/products', methods=['GET'])
    def get_all_products():
        products = product_use_case.get_all()
        return jsonify([product.to_dict() for product in products])

    @app.route('/products/<string:product_id>', methods=['DELETE'])
    def eliminate_product(product_id):
        product_use_case.eliminate(product_id)
        return '', 204