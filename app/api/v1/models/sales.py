
sales = []

class SalesData():
    def save_sale(self,category, product_name, quantity, price):
        salesId = len(sales)+1
        sales_cart = { 
            "salesId":salesId,
            "category":category, 
            "product_name":product_name, 
            "quantity":quantity,
            "price":price
        }
        sales.append(sales_cart)
        return sales_cart
    
    def get_sales(self):
        return sales