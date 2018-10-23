import json
from .base_tests import BaseTest

class TestSales(BaseTest):

    # a store attendant should post a sale record
    def test_postsale(self):
        with self.client:
            response = self.client.post(
                '/api/v1/sales',
                headers=dict(Authorization = "Bearer " + self.token_attendant), 
                data = json.dumps(self.sale),
                content_type='application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200, result['response'])
    
    # test that a store owner to fetch all sale records
    def test_get_sale(self):
        with self.client:
            response = self.client.get(
                '/api/v1/sales',
                headers=dict(Authorization = "Bearer " + self.token_owner), 
                content_type = 'application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200, result['Sales'])
    
    # test that a store admin to fetch all sale records
    def test_admin_get_sale(self):
        with self.client:
            response = self.client.get(
                '/api/v1/sales',
                headers=dict(Authorization = "Bearer " + self.token_admin), 
                content_type = 'application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200, result['Sales'])
    
    # test that owner can fetch a single sale
    def test_owner_getSingleSale(self):
        with self.client:
            response = self.client.get(
                '/api/v1/sales/sales1',
                headers=dict(Authorization = "Bearer " + self.token_owner), 
                content_type = 'application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200, result['response'])

    # test that owner can fetch a single sale
    def test_admin_getSingleSale(self):
        with self.client:
            response = self.client.get(
                '/api/v1/sales/sales1',
                headers=dict(Authorization = "Bearer " + self.token_admin), 
                content_type = 'application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200, result['response'])