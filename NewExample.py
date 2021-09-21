# from array import *
#
# # myList = ['vani','kavya','chaturvi']
#
#
# s1 = 'vani'
# s2 = 'kavya'
# s3 = 'chaturvi'
# i = 0
# j = 0
# k = 0
# for i in range(0, len(s1)):
#     for j in range(0, len(s2)):
#         for k in range(0, len(s3)):
#             print(s1[i],s2[j],s3[k])

# while len(s1):
#     while len(s2):
#         while len(s3):
#             print(s1[i], end="")
#             print(s2[j], end="")
#             print(s3[k], end="")


# list = []
# n = int(input("Enter the number of names you want enter: "))
#
# for x in range(n):
#     x = input("Enter the next name: ")
#     list.append(x.capitalize())
#
# print(list)

from num2words import num2words
#loc = "C:\\Users\\kothapalli.vanisree\\OneDrive - HCL Technologies Ltd\\Desktop\\NewTextfile.txt"
# file = open("NewTextfile.txt",'r+')
#file.truncate(0)

# file = open("NewTextfile.txt",'w')
# file.write("4321")

file = open("NewTextfile.txt",'r')
num = file.read()
file.close()

str = num2words(num)
file = open("NewTextfile.txt",'a')
file.write(str)
file.close()

file = open("NewTextfile.txt",'r')
print(file.read())










