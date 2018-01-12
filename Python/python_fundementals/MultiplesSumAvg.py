def Multiples():
    for i in range(1, 1001, 2):
        print (i)
#Multiples()

def MultiplesOf():
    for j in range(0, 1000000, 5):
        print (j)
#MultiplesOf()

def Average(): #returns average of values in THIS list
    arr = [1, 2, 5, 10, 255, 3]
    Sum = sum(arr)
    avg = Sum / len(arr)
    print (avg)
Average()