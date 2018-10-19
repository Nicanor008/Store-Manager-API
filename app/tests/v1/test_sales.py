import unittest 
import json
from app import create_app
from instance.config import app_config


class TestSales(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        self.sale = {
            "salesId":"sales1", 
            "category":"Laptops", 
            "product_name":"HP Acer 844C", 
            "quantity":1,
            "price":1000
        }

    # def test_postsale(self):
    #     with self.client:
    #         response = self.client.post(
    #             '/api/v1/sales', 
    #             data = json.dumps(self.sale),
    #             headers={'content_type':'application/json'}
    #         )
    #         result = json.loads(response.data.decode('utf-8'))
    #         self.assertEqual(response.status_code, 200, result['response'])
    

    # def test_get_sale(self):
    #     with self.client:
    #         response = self.client.get(
    #             '/api/v1/sales',
    #             headers={'content_type':'application/json'}
    #         )
    #         result = json.loads(response.data.decode('utf-8'))
    #         self.assertEqual(response.status_code, 200, result['Sales'])
    
    # def test_getSingleSale(self):
    #     with self.client:
    #         response = self.client.get(
    #             '/api/v1/sales/sales1',
    #             headers={'content_type':'application/json'}
    #         )
    #         result = json.loads(response.data.decode('utf-8'))
    #         self.assertEqual(response.status_code, 200, result['response'])