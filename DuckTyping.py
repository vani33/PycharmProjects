# class Duck:
#     def quack(self):
#         print('Quack, Quack....')
#
#
# class Monkey:
#     def talk(self):
#         print('monkey talking like a duck: Quack,Quack...')
#
#
# def invoke_quack(object):
#     #Non-Pythonic code
#     if hasattr(object,'quack'):
#         if callable(object.quack()):
#             object.quack()
#
#     #Pythonic code:EAFP
#     try:
#        object.quack()
#     except AttributeError as e:
#        print(e)
#
# d = Duck()
# m = Monkey()
# invoke_quack(d)
# invoke_quack(m)


#student = {'name':'Vani','marks':98,'rollno':101}
student = {'name':'Vani','rollno':101}
#Non-Pythonic code(LBYL-Look Before You Leave)
#This code is lengthy and there will be a performance issue
if 'name' in student and 'marks' in student and 'rollno' in student:
    print('Hello I am {name}, My Rollno: {rollno}, My Marks:{marks}'.format(**student))
else:
    print('Missing Some keys')

#Pythonic(EAFP)
try:
    print('Hello I am {name}, My Rollno: {rollno}, My Marks:{marks}'.format(**student))
except KeyError as e:
    print('Missing {} key'.format(e))

#This is Non-pythonic code because it checks everytime
def print4th_index_element(list):
    if len(list)>=5:
        print(list[4])
    else:
        print('There is no such element')

#This is pythonic code
def print4th_index_element(list):
    try:
        print(list[4])
    except IndexError:
        print('There is no such element')









