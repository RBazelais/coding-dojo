'''
Find and replace
print the position of the first instance of the word "day". 
Then create a new string where the word "day" is replaced 
with the word "month".
'''
words = "It's thanksgiving day. It's my birthday,too!"
str1 = words.replace("day", "month")
#print str1

#Min and Max
#Print the min and max values in a list like this one: 
#x = [2,54,-2,7,12,98]. Your code should work for any list.
x = [2, 54, -2, 7, 12, 98]
def MinAndMax():
    Min = min(x)
    Max = max(x)
    print "The smallest value is ", Min
    print "The largest value is ", Max
#MinAndMax()

#Print the first and last values in a list like this one: 
#x = ["hello",2,54,-2,7,12,98,"world"]. 
#Now create a new list containing only the first and last values in the original list. 
#Your code should work for any list.

x = ["hello",2,54,-2,7,12,98,"world"]
def FirstAndLast(x):
    newList = [] 
    length = len(x)
    newList.append(x[0])
    newList.append(x[length-1])
    print newList
#FirstAndLast(x)

#New List
#Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. 
#Sort your list first. Then, split your list in half. 
#Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!

def makeNewList():
    x = [19,2,54,-2,7,12,98,32,10,-3,6]
    x.sort()
    #[-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
    index = len(x)/2
    
    firstHalf = x[:index]
    secondHalf = x[index:]
    # colon notation takes a subset of the index
    
    print firstHalf
    print secondHalf

    secondHalf.insert(0, firstHalf)
    print secondHalf

makeNewList()

    