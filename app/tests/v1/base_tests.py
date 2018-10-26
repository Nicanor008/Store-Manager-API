import unittest 
import json
from app import create_app


class BaseTest(unittest.TestCase):

    def setUp(self):
        # self.app = create_app(config_name="testing")
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        self.products = {
            "category":"laptops",
            "name":"Acer Laptop"
        }
        self.sale = {
            "category":"Laptops", 
            "product_name":"HP Acer 844C", 
            "quantity":1,
            "price":1000
        }
        
        # users base url
        self.register_url = '/api/v1/auth/register'
        self.login_url = '/api/v1/auth/login'

        # base url(s) for products tests
        self.products_url = 'api/v1/products'
        self.get_single_product = '/api/v1/products/1'
        self.get_unavailable_product = '/api/v1/products/12323'
        self.get_string_productid = '/api/v1/products/sdfs'

        # base url(s) for sales tests
        self.sales_url = '/api/v1/sales'
        self.get_single_sale = '/api/v1/sales/1'

    # Store Owner register
        self.owner_register = self.client.post(
            self.register_url,
            data=json.dumps(dict(
                name="Elsie Chep",
                username="Eldie",
                email="elsie@gmail.com",
                password="elsie",
                role="owner"
            )),
            content_type='application/json'
        )
        # Store Owner login
        self.owner_response = self.client.post(  
            '/api/v1/auth/login',
            data=json.dumps(dict(
                email='elsie@gmail.com',
                password='elsie'
            )),
            content_type='application/json'
        )
        result_owner = json.loads(self.owner_response.data.decode('utf-8'))
        self.token_owner = result_owner["token"]

        # Store admin register
        self.admin_register = self.client.post(
            self.register_url,
            data=json.dumps(dict(
                name="Nicque Kip",
                username="nicque",
                email="nicque@nic.com",
                password="nicque",
                role="admin"
            )),
            content_type='application/json'
        )
        # Store admin login
        self.admin_response = self.client.post(  
            '/api/v1/auth/login',
            data=json.dumps(dict(
                email='nicque@nic.com',
                password='nicque'
            )),
            content_type='application/json'
        )
        result_admin = json.loads(self.admin_response.data.decode('utf-8'))
        self.token_admin = result_admin["token"]

        # Store Attendant registered
        self.attendant_register = self.client.post(
            self.register_url,
            data=json.dumps(dict(
                name="Nicanor KK",
                username="Nic",
                email="nic@nic.comm",
                password="nicki",
                role="attendant"
            )),
            content_type='application/json'
        )
        # Store attendant login
        self.attendant_response = self.client.post(  
            self.login_url,
            data=json.dumps(dict(
                email='nic@nic.com',
                password='nicki'  
            )),
            content_type='application/json'
        )
        result_attendant = json.loads(self.admin_response.data.decode('utf-8'))
        self.token_attendant = result_attendant["token"]
        
