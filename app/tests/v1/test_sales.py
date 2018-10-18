from flask import Flask
import unittest 
import json
from app import create_app
from instance.config import app_config

app = Flask(__name__)

class TestSales(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.sale = {
            'salesId':'sale1',
            'category':'laptops',
            'name':'Acer Laptop',
            'quantity':2,
            'price':20000
        }

    def test_postsale(self):
        with self.client:
            response = self.client.post(
                '/api/vi//sales', 
                data = json.dumps(self.sale),
                headers={'content_type':'application/json'}
            )
            # result = json.loads(response.data)
            self.assertEqual(response.json, {'New Product':{'productid':'la01','category':'laptops','name':'Acer Laptop'}})
            # self.assertTrue(result['status'], 'success')
            self.assertEqual(response.status_code, 201)
    

    def test_get_sale(self):
        with self.client:
            response = self.client.get(
                '/api/vi//sales',
                headers={'content_type':'application/json'}
            )
            self.assertEqual(response.status_code, 200)
    
    # def test_getSingleProduct(self):
    #     with self.client:
    #         response = self.client.get(
    #             '/api/vi//sales/<salesId>',
    #             headers={'content_type':'application/json'}
    #         )