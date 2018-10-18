from flask import Flask
import unittest 
import json
from app import create_app
from instance.config import app_config

app = Flask(__name__)

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.products = {
            'productid':'la01',
            'category':'laptops',
            'name':'Acer Laptop'
        }

    def test_postproduct(self):
        with self.client:
            response = self.client.post(
                '/api/vi/products', 
                data = json.dumps(self.products),
                headers={'content_type':'application/json'}
            )
            # result = json.loads(response.data)
            self.assertEqual(response.json, {'New Product':{'productid':'la01','category':'laptops','name':'Acer Laptop'}})
            # self.assertTrue(result['status'], 'success')
            self.assertEqual(response.status_code, 201)
    

    def test_get_product(self):
        with self.client:
            response = self.client.get(
                '/api/vi/products',
                headers={'content_type':'application/json'}
            )
            self.assertEqual(response.status_code, 200)
    
    # def test_getSingleProduct(self):
    #     with self.client:
    #         response = self.client.get(
    #             '/api/vi/products/<productId>',
    #             headers={'content_type':'application/json'}
    #         )