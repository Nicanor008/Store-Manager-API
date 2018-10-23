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
            "productId":"la01",
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

    # Store Owner register
        self.owner_register = self.client.post(
            '/api/v1/auth/register',
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
            '/api/v1/auth/register',
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
            '/api/v1/auth/register',
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
            '/api/v1/auth/login',
            data=json.dumps(dict(
                email='nic@nic.com',
                password='nicki'  
            )),
            content_type='application/json'
        )
        result_attendant = json.loads(self.admin_response.data.decode('utf-8'))
        self.token_attendant = result_attendant["token"]
        
