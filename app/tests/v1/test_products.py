import json
from base_tests import BaseTest

class TestProduct(BaseTest):
    # Test fetch product API endpoint and only accessible to admin and owner
    # Store admin to add a product
    def test_admin_postproduct(self):
        with self.client:
            response = self.client.post(
                'api/v1/products', 
                headers=dict(Authorization = "Bearer " + self.token_admin),
                data = json.dumps(self.products),
                content_type='application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200, result['response'])

    # Store Owner to add a product
    def test_owner_postproduct(self):
        with self.client:
            response = self.client.post(
                'api/v1/products', 
                headers=dict(Authorization = "Bearer " + self.token_owner),
                data = json.dumps(self.products),
                content_type='application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200, result['response'])

    # If a normal attendant tries to add a product, this should fail and prompt a user
    # def test_attendant_postproduct(self):
    #     with self.client:
    #         response = self.client.post(
    #             'api/v1/products', 
    #             headers=dict(Authorization = "Bearer " + self.token_attendant),
    #             data = json.dumps(self.products),
    #             content_type='application/json'
    #         )
    #         result = json.loads(response.data.decode('utf-8'))
    #         result[""]
    #         self.assertEqual(response.status_code, 200, result['response'])
    
    #admin to fetch products 
    def test_admin_get_product(self):
        with self.client:
            response = self.client.get(
                '/api/v1/products',
                headers=dict(Authorization = "Bearer " + self.token_admin),
                content_type='application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200, result['Products'])

    #Store attendant to fetch all products 
    def test_attendant_get_product(self):
        with self.client:
            response = self.client.get(
                '/api/v1/products',
                headers=dict(Authorization = "Bearer " + self.token_attendant),
                content_type='application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200, result['Products'])

    #Store Owner to access products 
    def test_owner_get_product(self):
        with self.client:
            response = self.client.get(
                '/api/v1/products',
                headers=dict(Authorization = "Bearer " + self.token_owner),
                content_type='application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200, result['Products'])
    
    # Store Owner to fetch a single product 
    def test_owner_getSingleProduct(self):
        with self.client:
            response = self.client.get(
                '/api/v1/products/la01',
                headers=dict(Authorization = "Bearer " + self.token_owner),
                content_type='application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200, result['response'])


    # Store Admin to fetch a single product 
    def test_admin_getSingleProduct(self):
        with self.client:
            response = self.client.get(
                '/api/v1/products/la01',
                headers=dict(Authorization = "Bearer " + self.token_admin),
                content_type='application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            res = result.get('productId')
            if res is '':
                self.assertEqual(response.status_code, 200, "cannot be null")
            if not res:
                self.assertEqual(response.status_code, 200, "failed")
            self.assertEqual(response.status_code, 200, result['response'])

    # Store attendant to fetch a single product 
    def test_attendant_getSingleProduct(self):
        with self.client:
            response = self.client.get(
                '/api/v1/products/la01',
                headers=dict(Authorization = "Bearer " + self.token_attendant),
                content_type='application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            res = result.get('productId')
            if not res:
                self.assertEqual(response.status_code, 200, "failed")
            self.assertEqual(response.status_code, 200, result['response'])