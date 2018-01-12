class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    
    #display the bike's price, 
    #maximum speed, and the total miles
    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles

    
    #display "Riding" on the screen and increase the 
    #total miles ridden by 10
    def ride(self):
        print "Riding " + (self.miles + 10)


    #display "Reversing" on the screen and decrease the 
    #total miles ridden by 5...
    def reverse(self):
        print "Reversing"
        self.miles -= 5

#created an instance of the class
Kwasaki_Ninja = Bike(7000, 210, 350)
Kwasaki_Ninja.displayInfo()
