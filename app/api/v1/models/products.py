
products = []

class ProductsData():
   def save_product(self, category, product_name, quantity, price):
       productId = len(products)+1
       # dictionary data structure for users products
       users_products = {
           "productId":productId,
           "category":category,
           "product_name":product_name,
           "quantity":quantity,
           "price":price
        }
       products.append(users_products)
        # products.append(users_products)
       return users_products
    
   def get_products(self):
       return products

#    def update_update(self, productid):
#        for product in products:
#            if product['productid'] == productid:
               