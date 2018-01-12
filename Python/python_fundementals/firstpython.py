#print 1 - 255
def oneto255():
    for x in range(1, 256):
        print(x)
#oneto255()

def odds1to255():
    for y in range(1, 256):
        if y % 2 != 0:
            print(y)
#odds1to255()

def intToSum():
    sum = 0
    for x in range(1, 256):
        sum += x
        print ("Num = ")
        print (x)
        print ("Sum = ")
        print (sum)
intToSum()
