# s = input('Enter the string:')
# s1 = s2 = output = ''
# for x in s:
#     if x.isalpha():
#         s1 = s1 + x
#     else:
#         s2 = s2 + x
# for x in sorted(s1):
#     output = output + x
# for x in sorted(s2):
#     output = output + x
# print(output)
####################################
# s = input('Enter the string: ')
# output = ''
# for x in s:
#     if x.isalpha():
#         output=output+x
#         previous = x
#     else:
#         output=output+previous*(int(x)-1)
# print(output)
#############################################
# s = input('Enter the string: ')
# output = ''
# for x in s:
#     if x.isalpha():
#         output=output+x
#         previous=x
#     else:
#         newch = chr(ord(previous)+ int(x))
#         output=output+newch
# print(output)
################################################
# s1 = input('Enter first string: ')
# s2 = input('Enter second string: ')
# output =''
# i = j = 0
# while i<len(s1) or j<len(s2):
#     output=output+s1[i]+s2[j]
#     i+=1
#     j+=1
# print(output)
###################################################
# s1 = input('Enter first string: ')
# s2 = input('Enter second string: ')
# output =''
# i = j = 0
# while i<len(s1) or j<len(s2):
#     if i<len(s1):
#         output=output+s1[i]
#         i+=1
#     if j < len(s2):
#         output = output+s2[j]
#         j+=1
# print(output)
###################################################
# list = []
# for x in range(1, 11):
#     list.append(x*x)
# print(list)

# l1 = [x*x for x in range(1,11)]
# print(l1)
####################################################
# l1 = [x**2 for x in range(1,21) if (x**2)%2==0]
# print(l1)
########################################################
# a = 10
# b = 20
# c = 30
# d = 40
# t = a,b,c,d
# print(t)
#########################################
# t  = (10,20,30,40)
# a,b,c,d = t
# print("a=",a, "b=",b, "c=",c, "d=",d)
#############################################
# t = eval(input("Enter some tuple of numbers: "))
# l = len(t)
# sum = 0
# for x in t:
#     sum = sum + x
# print("The sum is: ", sum)
# print("Average is: ",sum/l)
##########################################################
# s = {10,20,30,40}
# l = [50, 60, 70]
# s.update(l,range(1,5), 'vani')
# print(s)
#
# s = {10,20,30,40}
# s1 = s.copy()
# print(id(s))
# print(id(s1))
#######################################################
# s1 = {10,20,30,40, 50}
# s2 = {10, 20, 30, 60, 70}
# print(s1.union(s2))
# print(s1|s2)
# print(s1.intersection(s2))
# print(s1-s2)
# print(s1.symmetric_difference(s2))
#######################################################
# l = eval(input("Enter the list values: "))
# s = set(l)
# print(s)
######################################################
# l = eval(input("Enter the list values: "))
# l1 = []
# for x in l:
#     if x not in l1:
#         l1.append(x)
# print(l1)
#################################################

# rec ={}
# n = int(input("Enter number of students: "))
# i = 1
# while i <= n:
#     name = input("Enter the Student Name: ")
#     marks = input("Enter % of marks: ")
#     rec[name] = marks
#     i += 1
# print("Name", "\t", "%of marks")
# for x in rec:
#     print(x, "\t\t", rec[x])
###################################################################
# dict = {100:'vani', 200:'kavya',300:'chaturvi'}
# print(dict)
# dict[400] = 'nirvi'
# print(dict)
# dict[100] = 'pushpa'
# print(dict)

# dict = {100:'vani', 200:'kavya',300:'chaturvi'}
# del dict[100]
# print(dict)
#
# dict.clear()
# print(dict)

# d = {100:'vani', 200:'kavya',300:'chaturvi'}
# d1 = {'a':'apple','b':'banana'}
# d.update(d1)
# print(d)
# d.setdefault(100, 'sunny')
# print(d)
# d.setdefault(400, 'sunny')
# print(d)
# print(d.items())
# print(d.values())
# print(d.pop(100))
# print(d)
# print(d.popitem())
# print(d)
# print(d.get(100))
# print(d.get(400))
# print(d.get(100, 'pushpa'))
# print(d.get(400, 'pushpa'))
# print(len(d))
#############################################################
# d = eval(input("Enter the dictionary: "))
# s = sum(d.values())
# print("Sum of values is: ",s)

#############################################################
# word = input("Enter some word: ")
# dict = {}
# for x in word:
#     dict[x] = dict.get(x,0) + 1
# #print(dict)
# for k,v in dict.items():
#     print("{} occred {} times".format(k,v))

#############################################################
# word = input("Enter some word: ")
# vowels = {'a', 'e', 'i', 'o', 'u'}
# d = {}
# for x in word:
#     if x in vowels:
#         d[x] = d.get(x,0) + 1
# for k,v in sorted(d.items()):
#     print("{} occurred {} times".format(k, v))


####################################################################

# n = int(input("Enter the number of students: "))
# d = {}
# for x in range(n):
#     name = input("Enter student name: ")
#     marks = int(input("Enter students marks: "))
#     d[name] = marks
# print(d)
# while True:
#     name = input("Enter student name to get marks: ")
#     marks = d.get(name, -1)
#     if marks == -1:
#         print("Student not available")
#     else:
#         print("The marks of {} is {}".format(name, marks))
#     option = input("Do you want to find another student marks[Yes][No]: ")
#     if option == "No":
#         break
# print("Thanks for using our application")
#####################################################################################
# squares = {x:x*x for x in range(1,6)}
# print(squares)








































































































































































