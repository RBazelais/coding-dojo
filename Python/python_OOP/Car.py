class Car(object):
    def __init__(self, price, speed, fuel, mileage, tax):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = tax
    
    #display the car's price, 
    #maximum speed, and the total mileage
    def displayAll(self):
        print "Price:", self.price
        print "Speed:", self.speed, "mph"
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage, "mpg"

        if self.price >= 10000:
            self.tax = 0.15
            print "Tax:", self.tax, "\n" 
        else:
            self.tax = 0.12
            print "Tax:", self.tax, "\n" 
        return self

#created an instance of the class
Impala = Car(2000, 35, "Full", 15, 0.2)
Hooptee = Car(2000, 5, "Not Full", 105, 0.2)
Impala.displayAll()
Hooptee.displayAll()
