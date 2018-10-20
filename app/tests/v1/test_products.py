import unittest 
import json
from app import create_app


class TestProduct(unittest.TestCase):

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

    def test_postproduct(self):
        with self.client:
            # admin registered
            self.client.post(
                '/api/v1/auth/register',
                data=json.dumps(dict(
                    name='nicanor kk',
                    email='nic@nic.com',
                    role='admin',
                    username='nic',
                    password='nic'
                )),
                content_type='application/json'
            )
            # get admins data
            admin_response = self.client.post(
                '/api/v1/auth/login',
                data=json.dumps(dict(
                    email='nic@nic.com',
                    password='nic'
                    
                )),
                content_type='application/json'
            )
            resultatt = json.loads(admin_response.data)
            token = resultatt["access_token"]
            response = self.client.post(
                'api/v1/products', 
                headers=dict(Authorization="Bearer " + token),
                data = json.dumps(self.products),
                content_type='application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200, result['response'])
    

    def test_get_product(self):
        with self.client:
            response = self.client.get(
                '/api/v1/products',
                headers=dict(Authorization="Bearer " + token),
                content_type='application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200, result['Products'])
    
    def test_getSingleProduct(self):
        with self.client:
            response = self.client.get(
                '/api/v1/products/la01',
                headers=dict(Authorization="Bearer " + token),
                content_type='application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200, result['response'])