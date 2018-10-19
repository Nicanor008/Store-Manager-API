# import unittest 
# import json
# from app import create_app
# from instance.config import app_config


# class TestProduct(unittest.TestCase):

#     def setUp(self):
#         # self.app = create_app(config_name="testing")
#         self.app = create_app()
#         self.app.testing = True
#         self.client = self.app.test_client()
#         self.products = {
#             "productId":"la01",
#             "category":"laptops",
#             "name":"Acer Laptop"
#         }

    # def test_postproduct(self):
    #     with self.client:
    #         response = self.client.post(
    #             'api/v1/products', 
    #             data = json.dumps(self.products),
    #             headers={'content_type':'application/json'}
    #         )
    #         result = json.loads(response.data.decode('utf-8'))
    #         self.assertEqual(response.status_code, 200, result['response'])
    

    # def test_get_product(self):
    #     with self.client:
    #         response = self.client.get(
    #             '/api/v1/products',
    #             headers={'content_type':'application/json'}
    #         )
    #         result = json.loads(response.data.decode('utf-8'))
    #         self.assertEqual(response.status_code, 200, result['Products'])
    
    # def test_getSingleProduct(self):
    #     with self.client:
    #         response = self.client.get(
    #             '/api/v1/products/la01',
    #             headers={'content_type':'application/json'}
    #         )
    #         result = json.loads(response.data.decode('utf-8'))
    #         self.assertEqual(response.status_code, 200, result['response'])