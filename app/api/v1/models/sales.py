
class SalesData():
    def __init__(self):
        self.sale=[
            {"salesId":"sales1", "category":"foodstuff", "product_name":"Pizza", "quantity":3, "price":400}
        ]
    
    def get_sales(self):
        return self.sale