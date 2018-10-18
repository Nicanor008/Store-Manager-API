import unittest 
import json
from app import create_app
from instance.config import app_config


class TestSales(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.app.testing = True
        self.client = self.app.test_client()
        
         self.products = {
            "productid":"la01",
            "category":"laptops",
            "name":"Acer Laptop"
        }

        self.sale = {
            "salesId":"sales1", 
            "category":"Laptops", 
            "product_name":"HP Acer 844C", 
            "quantity":1,
            "price":1000
        }