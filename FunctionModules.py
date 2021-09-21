# def calc(a,b):
#     sum = a+b
#     sub = a-b
#     mul=a*b
#     div = a/b
#     return sum,sub,mul,div
# a,b,c,d = calc(100,50)
# print(a,b,c,d)

# def calc(a,b):
#     sum = a + b
#     return sum
# t = calc(a = 100, b = 50)
# t = calc(b = 50,a = 100)

# def wish(msg, name="Guest"):pass

# def sum(*n,name):
#      result = 0
#      for x in n:
#          result = result + x
#      print("The sum by {} is:{} ".format(name, result))
# sum(name ='vani')
# sum(10, name ='kavya')
# sum(10,20,name='chaturvi')
# sum(10,20,30,name='sunny')
# sum(10,20,30,40,name='bunny')
###############################################################
# def display(**x):
#     print("Record Information:")
#     for k,v in x.items():
#         print(k,"..........",v)
# display(name='vani',marks=100,age=22)
# display(name='kavya',gender='female',city='Tirupati')
# display(name='chaturvi',phoneno='123456789',state='AP')
###################################################################
# def factorial(n):
#     if(n == 0):
#         result =1
#     else:
#         result = n * factorial(n-1)
#     return result
# print(factorial(0))
# print(factorial(5))

########################################################################
# def squareIt(n):
#     return n*n
#
# s = lambda n:n*n
# print(s(4))

# s = lambda x:x*x
# print(s(2))
# print(s(3))
# print(s(4))

# s = lambda a,b:a+b
# print(s(2,4))
# s= lambda a,b: a if a>b else b
# print("Biggest of two given numbers is: ",s(10,20))

# def iseven(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# l = [0,10,4,3,9,8]
# l1 = list(filter(iseven, l))
# print(l1)

# l = [0,10,4,3,9,8]
# l1 = list(filter(lambda x:x%2==0, l))
# print(l1)

# def double(x):
#     return 2*x
# l =[1,2,3,4,5]
# l1 = list(map(double, l))
# print(l1)
#
# l =[1,2,3,4,5]
# l1 = list(map(lambda x:2*x, l))
# print(l1)

# l1 = [1,2,3,4]
# l2 = [10,20,30,40]
# l3 = list(map(lambda x,y:x*y, l1,l2))
# print(l3)
#
# def f1():
#     def inner(a,b):
#         print("The sum: ", a+b)
#         print("The avg: ",(a+b)/2)
#         print()
#     inner(10,20)
#     inner(20,30)
# f1()
# ############################################################
# def outer():
#     print("Outer function started")
#     def inner():
#         print("inner function execution")
#     print("outer function returning inner function")
#     return inner
# f1 = outer()
# f1()
#
# def decor(func):
#     def inner(name):
#         if name=='kavya':
#             print("Hello {} Bad Morning!".format(name))
#         else:
#             func(name)
#     return inner
#
# #@decor
# def wish(name):
#     print("Hello {} Good morning".format(name))
# wish('vani')
# wish('kavya')
# wish('chaturvi')
#
# decorfunction = decor(wish)
####################################################################
# def smartdivision(func):
#     def inner(a,b):
#         if b == 0:
#             print("We cannot divide with zero")
#         else:
#             return func(a,b)
#     return inner
#
# @smartdivision
# def division(a,b):
#     return a/b
# print(division(10,2))
# print(division(10,0))
############################################################################
# #Module Program
# print("This is the Module program")
#
# #Test class
# import module1
# import module1
# import module1
# import module1
# import module1
# import module1
# print("This the Test Module")
###############################################################################
# import time
# from imp import reload
# import module1
# print("program entering into sleeping state")
# time.sleep(30)
# reload(module1)
# print("This is the last line of program")
#################################################################################
# x = 10
# y = 20
# def f1():
#     print("Hello")
# print(dir())
#
# print(__name__)
# print(__package__)
###############################################################################
# from math import *
# print(sqrt(4))
# print(ceil(10.1))
# print(floor(10.1))
# print(fabs(-10.6))#float absolute value
# print(fabs(10.6))
###############################################################################
# from random import *
# list = ["vani", "kavya", "chaturvi", "pushpa"]
# for i in range(5):
#     print(choice(list))
#     #print(uniform(1,3))
#     #print((randint(1, 10))

from random import *
for i in range(10):
    print(chr(randint(65,65+25)),randint(0,10),chr(randint(65,65+25)),randint(0,10),chr(randint(65,65+25)),randint(0,10), sep='')

from random import *
for i in range(10):
    print(randint(100000,999999))




























































































