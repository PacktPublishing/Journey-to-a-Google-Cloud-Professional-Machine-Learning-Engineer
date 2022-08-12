import math

# find all the PNs in (a,b)
def PNlist(a,b):
    list=[]
    for Number in range (a, b):
        if (Prime(Number)==1):
            list.append(Number)
    return list

# Check if Number is a prime
def Prime(Number):
    for i in range(2, (int(math.sqrt(Number))+1)):
        if(Number % i == 0):
           return 0
        else: 
           continue
    return 1

list1=PNlist(1,100) 
print(list1)
