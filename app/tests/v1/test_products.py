import json
from app.tests.v1.base_tests import BaseTest

class TestProduct(BaseTest):
    # Test fetch product API endpoint and only accessible to admin and owner
    # Store admin to add a product
    def test_admin_postproduct(self):
         # Store admin register
        admin_register = self.client.post(
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
        json.loads(admin_register.data)
        # Store admin login
        admin_response = self.client.post(  
            self.login_url,
            data=json.dumps(dict({
                'email':'nicque@nic.com',
                'password':'nicque'
            })),
            content_type='application/json'
        )
        result_admin = json.loads(admin_response.data.decode('utf-8'))
        token_admin = str(result_admin.get("token"))
        # token_admin = result_admin["token"]

        with self.client:
            response = self.client.post(
                self.products_url, 
                headers = (dict(Authorization = 'Bearer ' + token_admin)),
                data = json.dumps(self.products),
                content_type='application/json'
            )
            result = json.loads(response.data)
            self.assertEqual(result.get('message'), 'New product added successfully')
            self.assertEqual(response.status_code, 200)


    
    #admin to fetch products 
    def test_admin_get_product(self):
        with self.client:
            response = self.client.get(
                self.products_url,
                headers=dict(Authorization = "Bearer " + self.token_admin),
                content_type='application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertTrue(result['message'] == 'New product added successfully')
            self.assertEqual(response.status_code, 200)

    #Store attendant to fetch all products 
    def test_attendant_get_product(self):
        with self.client:
            response = self.client.get(
                self.products_url,
                headers=dict(Authorization = "Bearer " + self.token_attendant),
                content_type='application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertTrue(result['message'] != 'Products')
            self.assertEqual(response.status_code, 200)

    #Store Owner to access products 
    def test_owner_get_product(self):
        with self.client:
            response = self.client.get(
                self.products_url,
                headers=dict(Authorization = "Bearer " + self.token_owner),
                content_type='application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200)
            # tests
    
    # # # Store Owner to fetch a single product 
    # # def test_owner_getSingleProduct(self):
    # #     with self.client:
    # #         response = self.client.get(
    # #             self.get_single_product,
    # #             headers=dict(Authorization = "Bearer " + self.token_owner),
    # #             content_type='application/json'
    # #         )
    # #         result = json.loads(response.data.decode('utf-8'))
    # #         self.assertEqual(response.status_code, 200)


    # # Store Admin to fetch a single product 
    # def test_admin_getSingleProduct(self):
    #     with self.client:
    #         response = self.client.get(
    #             self.get_single_product,
    #             headers=dict(Authorization = "Bearer " + self.token_admin),
    #             content_type='application/json'
    #         )
    #         result = json.loads(response.data.decode('utf-8'))
    #         res = result.get('productId')
    #         self.assertEqual(response.status_code, 200)

    # # Store attendant to fetch a single product 
    # def test_attendant_getSingleProduct(self):
    #     with self.client:
    #         response = self.client.get(
    #             self.get_single_product,
    #             headers=dict(Authorization = "Bearer " + self.token_attendant),
    #             content_type='application/json'
    #         )
    #         result = json.loads(response.data.decode('utf-8'))
    #         self.assertEqual(response.status_code, 200)

    # # test if product fetched is not available
    # def test_SingleproductNotAvailable(self):
    #     with self.client:
    #         response = self.client.get(
    #             self.get_unavailable_product,
    #             headers=dict(Authorization = "Bearer " + self.token_attendant),
    #             content_type='application/json'
    #         )
    #         result = json.loads(response.data.decode('utf-8'))
    #         self.assertTrue(result['response'] == 'Product Not Available')
    #         self.assertEqual(response.status_code, 200)

    #  # test if product fetched is not available
    # def test_SingleproductIdIsString(self):
    #     with self.client:
    #         response = self.client.get(
    #             self.get_string_productid,
    #             headers=dict(Authorization = "Bearer " + self.token_attendant),
    #             content_type='application/json'
    #         )
    #         result = json.loads(response.data.decode('utf-8'))
    #         self.assertEqual(result['message'], 'Product ID should be an integer')
    #         self.assertEqual(response.status_code, 200)