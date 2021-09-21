# try:
#     print("Outer try block")
#     try:
#         print("Inner try block")
#         print(10/0)
#     except ZeroDivisionError:
#         print("Inner Except block")
#     finally:
#         print("Inner finally block")
# except:
#     print("Outer except block")
# finally:
#     print("Outer finally block")
############################################################################################

# try:
#     stmt-1
#     stmt-2
#     stmt-3
#     try:
#         stmt-4
#         stmt-5
#         stmt-6
#     except xxx:
#         stmt-7
#     finally:
#         stmt-8
#     stmt-9
# except yyy:
#     stmt-10
# finally:
#     stmt-11
# stmt-12
#
# case 1: if there is no exception, All stmts executed except 7 and 10.
# case 2: if an exception raised at stmt-2 and corresponding except block matched, stmts executed are 1,10,11,12.
#         control does not enter into inner try block.
# case 3: if an exception raised at stmt-2 and corresponding except block not matched, stmts executed are 1,11,12.
#         abnormal termination occurs because except block not matched, still finally block will execute.
# case 4: if an exception raised at stmt-5 and corresponding inner except block matched, stmts executed are 1,2,3,4,
#         7,8,9,11 and 12.
# case 5: if an exception raised at stmt-5 and inner except block not matched, but outer except block matched, stmts
#         executed are 1,2,3,4,8,10,11,12.
# case 6: if an exception raised at stmt-5 and both inner and outer except blocks not matched, stmts executed are 1,2,
#         3,4,8,11.
# case 7: if an exception raised at stmt-7 and corresponding except block matched, stmts executed are 1,2,3,8,10,11,12.
# case 8: if an exception raised at stmt-7 and corresponding except block not matched, stmts executed are 1,2,3,8,11.
# case 9: if an exception raised at stmt-8 and corresponding except block matched, stmts executed are 1,2,3,10,11,12.
# case 10: if an exception raised at stmt-8 and corresponding except block not matched, stmts executed are 1,2,3,11.
# case 11: if an exception raised at stmt-9 and corresponding except block matched, stmts executed are 1,2,3,8,10,11,12.
# case 12: if an exception raised at stmt-9 and corresponding except block not matched, stmts executed are 1,2,3,8,11.
# case 13: if an exception raised at stmt-10, then it always abnormal termination but before that finally block(stmt-11)
#          will be executed.
# case 14: if an exception raised at stmt-11 or stmt-12 then it is always abnormal termination.

#################################################################################################################
# try:
#     Risky code
# except:
#     will be executed if exception in try
# else:
#     will be executed if no exception in try
# finally:
#     will be executed always whether exception raised or not
#####################################################################################################3
# try:
#     print("try")
#     print(10/0)
# except:
#     print("except")
# else:
#     print("else")
# finally:
#     print("finally")
################################################################################################3
# try:
#     print("try")
#     print(10/0)
# finally:
#     print("finally")

# try:
#     print("try")
# except:
#     print("except")
# try:
#     print("inner try")
# else:
#     print("inner else")

# try:
#     print("try")
#     try:
#         print("inner try")
# except:
#     print("except")
# finally:
#     print("finally")

#########################################################################################
# class TooYoungException(BaseException):
#     def __init__(self,arg):
#         self.msg = arg
# class TooOldException(BaseException):
#     def __init__(self,arg):
#         self.msg = arg
#
# age = int(input("Enter age: "))
# if age < 18:
#     raise TooYoungException("Please wait some more time definetly you will get best match")
# elif age > 60:
#     raise TooOldException("Your age already crossed")
# else:
#     print("Thanks for registration")

###################################################################################################
# import logging
# logging.basicConfig(filename='log.txt', level=logging.WARNING)
# print("Python logging demo")
# logging.debug("Debug message")
# logging.info("Debug message")
# logging.warning("Debug message")
# logging.error("Debug message")
# logging.critical("Debug message")
#############################################################################################
# import logging
# logging.basicConfig(filename='log1.txt', level=logging.INFO)
# logging.info("A new request came")
# try:
#     x = int(input("Enter the first number: "))
#     y = int(input("Enter the second number: "))
#     print(x/y)
# except ZeroDivisionError as msg:
#     print("Cannot divide by zero")
#     logging.exception(msg)
# except ValueError as msg:
#     print("Enter only int values")
#     logging.exception(msg)
# logging.info("Request processing completed")
#########################################################################################
# import pickle
# class Employee:
#     def __init__(self, eno, ename,esal,eaddr):
#         self.eno = eno
#         self.ename = ename
#         self.esal = esal
#         self.eaddr = eaddr
#     def display(self):
#         print(self.eno, "\t", self.ename, "\t", self.esal, "\t", self.eaddr)
# #adv of with keyword in files is no need to close the file
# #wb is writebinary
# with open("emp.dat", "wb") as f:
#     e = Employee(100,'vani', 10000, 'Tirupati')
#     pickle.dump(e,f)
#     print("Pickling of employee object completed")
# with open("emp.dat", "rb") as f:
#     obj = pickle.load(f)
#     print("Employee Information after unpickling....")
#     obj.display()
#########################################################################################################
# import Emp,pickle
# f = open("emp.dat","wb")
# n = int(input("Enter number of employees: "))
# for i in range(n):
#     eno = int(input("Enter Employee number: "))
#     ename = input("Enter Employee name: ")
#     esal = float(input("Enter Employee salary: "))
#     eaddr = input("Enter Employee Address: ")
#     e = Emp.Employee(eno, ename, esal, eaddr)
#     pickle.dump(e,f)
#
# import Emp,pickle
# f = open("emp.dat", "rb")
# print("Employee Details: ")
# while True:
#     try:
#         obj = pickle.load(f)
#         obj.display()
#     except EOFError:
#         print("All Employess completed")
#         break
# f.close()
##############################################################################################
# class Employee:
#     def __init__(self,eno,ename):
#         self.eno = eno
#         self.ename=ename
#         print("Constructor execution")
#     def display(self):
#         print("Employee No: ",self.eno)
#         print("Employee Name: ",self.ename)
# e1 = Employee(100,'Vani')
# e2 = Employee(200,'Kavya')
# e1.display()
# e2.display()
#################################################################################################

# class Student:
#     def __init__(self, name, roll, marks):
#         self.name = name
#         self.roll = roll
#         self.marks = marks
#     def display(self):
#         print("Student name: ", self.name)
#         print("Student Rollno: ", self.roll)
#         print("Student Marks: ", self.marks)
#         print()
# s1 = Student('Vani', 95, 100)
# print(s1.__dict__)#used to display the object values in dict form
# s2 = Student('Kavya',200, 87)
# s3 = Student('Chaturvi',300,70)
# s1.display()
# s2.display()
# s3.display()
# print(s1.name,s1.rollno,s1.marks)#access from outside of class

# class Test:
#     def __init__(self):
#         self.a=100
#         self.b=200
#     def m1(self):
#         self.c=300
#         self.d=400
# t1 = Test()
# print(t1.__dict__)
# t1.m1()
# print(t1.__dict__)
# t1.e=500
# t1.f=600
# print(t1.__dict__)
# t2 = Test()
# print(t2.__dict__)
#########################################################################
# class Test:
#     def __init__(self):
#         self.a=100
#         self.b=200
#         self.c = 300
#         self.d = 400
# t1 = Test()
# t2 = Test()
# del t1.c
# print(t1.__dict__)
# print(t2.__dict__)

# class Student:
#     cname = 'Vidyanikethan'#Static variable
#     def __init__(self, name, roll, marks):
#         self.name = name
#         self.roll = roll
#         self.marks = marks

# class Test:
#     a = 10
#     def __init__(self):
#         self.b=20
#         Test.c = 30
#     def m1(self):
#         self.d =40
#         Test.e = 50
#     @classmethod
#     def m2(cls):#we can use any name instead of cls
#         cls.f =60 #f and g both are static variables
#         Test.g=70
#     @staticmethod
#     def m3():
#         Test.h=80
# t1 = Test()
# t1.m1()
# Test.m2()
# Test.m3()
# Test.i = 90 #outside of class
# print(Test.__dict__)
# print("t1:",t1.a,t1.b)
# print("t2:",t2.a,t2.b)
# Test.a = 888
# t1.b = 999
# print("t1:",t1.a,t1.b)
# print("t2:",t2.a,t2.b)

# class Test:
#     a = 10
#     def __init__(self):
#         print(self.a)
#         print(Test.a)
#
#     def m1(self):
#         print(self.a)
#         print(Test.a)
#
#     @classmethod
#     def m2(cls):#we can use any name instead of cls
#         print(cls.a)
#         print(Test.a)
#
#     @staticmethod
#     def m3():
#         print(Test.a)
#
# t1 = Test()
# print(t1.a)
# print(Test.a)

# class Test:
#     a = 10
#     def __init__(self):
#         self.b=20
# t1=Test()
# t2=Test()
# t1.a=888#it will not modify the static variable 'a' instead it checks for the instance variable 'a'
# #if it is not present then it will create the instance variable 'a'
# t1.b=999 #it will replace the value of 'b'
# print(t2.a,t2.b)#10,20
# print(t1.a,t1.b)#10,999
# print(t1.__dict__)
# print(t2.__dict__)

####################################################################################################3
# import re
# count=0
# # pattern = re.compile('ab')
# # matcher=pattern.finditer('abaababa')
# matcher = re.finditer('ab','abaababa')
# for match in matcher:
#     count+=1
#     #print("match is available at start index:",match.start())
#     print("start:{},end:{},group:{}".format(match.start(),match.end(),match.group()))
# print("number of occurrences of ab in given string:",count)


# import re
# matcher=re.finditer('a{1,3}','abaababa')
# for m in matcher:
#     print(m.start(),'......',m.group())


# import re
# s = input("Enter the pattern to check: ")
# m = re.match(s,'abcdefgh')
# if m!=None:
#     print("Match is available at the begining of the string")
#     print('Start Index:{} and End index:{}'.format(m.start(),m.end()))
# else:
#     print('Match is not available at the beginning of the string')

# import re
# s = input("Enter the pattern to check: ")
# m = re.fullmatch(s,'abcdefgh')
# if m!=None:
#     print("Full string matched")
#     print('Start Index:{} and End index:{}'.format(m.start(),m.end()))
# else:
#     print(' Full string not matched')

# import re
# s = input("Enter the pattern to check: ")
# m = re.search(s,'abaababaa')
# if m!=None:
#     print("Match is available")
#     print('Start Index:{} and End index:{}'.format(m.start(),m.end()))
# else:
#     print(' doesnt match')

# import re
# l = re.findall('[0-9]','a7b9k6z')
# print(l)

# import re
# t= re.subn('\d','#','ab3n5k9')
# print(type(t))
# print("The result string: ",t[0])
# print("number of replacements: ",t[1])


# import re
# l = re.split('-','10-20-30-40-50')
# print(l)

# import re
# s = input("Enter Identifier to validate: ")
# m = re.fullmatch('[a-k][0369][a-zA-Z0-9#]*',s)
# if m!=None:
#     print("s is valid ")
# else:
#     print("s is not valid")

# import re
# s = input("Enter mobile number to validate: ")
# m = re.fullmatch('[6-9]\d{9}',s)
# if m!=None:
#     print("s is valid mobile number")
# else:
#     print("s is not valid mobile number")


# import re
#
# s = input("Enter mobile number to validate: ")
# m = re.fullmatch('^(0|91|\+91)?[6-9]\d{9}', s)
# if m != None:
#     print("s is valid mobile number")
# else:
#     print("s is not valid mobile number")

# import re
# f1 = open('input.txt','r')
# f2 = open('output.txt','w')
# for line in f1:
#     list = re.findall('[6-9]\d{9}',line)
#     for number in list:
#         f2.write(number,"\n")
# print("Extracted all mobile numbers into output.txt")
# f1.close()
# f2.close()



# import re,urllib
# import urllib.request
# sites = ["http://google.com","http://rediff.com"]
# for s in sites:
#     print("Searching.....",s)
#     u = urllib.request.urlopen(s)
#     text = u.read()
#     title=re.findall("<title>.*</title>",str(text),re.IGNORECASE)
#     print(title[0])

# import re
# s = input("Enter mail id: ")
# m = re.fullmatch('\w[a-zA-Z0-9_.]*@gmail[.]com',s)
# if m!=None:
#     print("Valid mail id")
# else:
#     print("Invalid mail id")

# import threading
# print('Current executing thread: ',threading.current_thread().getName())

# from threading import *
# def display():
#     print('This code executed by Thread: ',current_thread().getName())#child thread
#
# t = Thread(target=display)#main thread creates child thread object
# #child thread object job is responsible to execute display method
# t.start()#main thread starts child thread
# print('This code executed by Thread: ',current_thread().getName())#main thread


# from threading import *
# def display():
#     for i in range(10):
#         print("CHILD THREAD",'\n')
# t=Thread(target=display)
# t.start()
# for i in range(10):
#     print("MAIN THREAD",'\n')



# from threading import *
#
# class MyThread(Thread):#Creating child class MyThread which extends Thread class
#     def run(self):#overriding the run method of Thread class
#         for i in range(10):
#             print('Child Thread-1')
#
# t = MyThread()
# t.start()
# for i in range(10):
#     print('Main Thread-1')


# from threading import *
#
# class Test:
#     def display(self):
#         for i in range(10):
#             print('Child Thread-1')
# obj = Test()
# t = Thread(target=obj.display)
# t.start()
# for i in range(10):
#     print('Main Thread-1')


# import threading
# print('Current executing thread: ',threading.current_thread().getName())
# threading.current_thread().setName('VaniThread')
# print(threading.current_thread().name)


# l1=[10,20,30,40]
# l2=l1
# l2[2]=70
# print(l1)
# print(l2)
#
# l1=[10,20,30,40]
# l2=l1.copy()#completely different object is created for l2 so, it wont change l1 contents
# l2[2]=70
# print(l1)
# print(l2)

# import copy
# l1=[10,20,[30,40],50]
# l2=copy.deepcopy(l1)
# l1[2][0]=888
# # l1[0]=111
# print("l1=",l1)
# print("l2=",l2)
# print(id(l1[2]))
# print(id(l2[2]))
# print(id(l1))
# print(id(l2))
# print(id(l1[0]))
# print(id(l2[0]))
































































































