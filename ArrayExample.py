#All values should be of same type
#Dynamic in size

#import array as arr
from array import *

values = array('i',[1,4,3,6,7])
#values = array('i',[1,4,3,-6,7])#possible
#values = array('I',[1,4,3,-6,7])#error
#values = array('i',[1,4,3.5,6,7])#error
print(values)
print(values.buffer_info())#this will print the size of an array with first argument as address and second
#argument as size.
print(values.typecode)#it will print the type of an array

for i in range(5):
    print(values[i])
for e in values:
    print(e)

values.reverse()#it will print the array values in reverse order.
print(values)

vals = array('u',['a','e','i','o','u'])#character array

newArr = array(values.typecode,(a for a in values))#creating the same array with same values
for k in newArr:
    print(k)

while i<len(values):
    print(newArr[i])
    i += 1


###########################################################################3

arr = array('i',[])

n = int(input("Enter the length of the array: "))
for x in range(n):
    y = int(input("Enter the next value: "))
    arr.append(y)

print(arr)


element = int(input("Enter the value for search: "))
for el in arr:
    if el == element:
        print(k)
        break
    k+=1
print(arr.index(element))#simplest way to print the index of the element we have entered.




str1 = "vani"
str2 = "kavya"
str3 = "chaturvi"

arr = array('s',[])
n = input("Enter the number of strings: ")
for str in range(n):
    y = input("Enter the next String: ")
    arr.append(y)
print(arr)







