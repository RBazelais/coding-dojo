class Product(object):
    def __init__(self, price, item_name, weight, brand, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
    
    def Sell(self):
        self.status = "sold"

    def Add_Tax(self):
        tax = self.price * 0.15
        print self.price + tax

    def Return(self, reason):
        if reason == "defective":
            self.price = 0
            self.status = "defective"
            
        elif reason == "sealed box":
            self.status = "For Sale"
            
        elif reason == "open box":
            self.status = "used"
            discount = self.price * .20
            self.price += discount
        print self.status

    def displayAll(self):
        print self.price
        print self.item_name
        print self.weight
        print self.brand
        print self.status

#created an instance of the class
Soap = Product(2.00, "soap", "3oz", "dove", "new")
Soap.displayAll()
Soap.Return("defective")