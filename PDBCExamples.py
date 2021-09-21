# import cx_Oracle
# connect = cx_Oracle.connect('scott/tiger@localhost')
# if connect!=None:
#     print('Connection established succesfully')
#     print('Version:',connect.version)
# else:
#     print('Connection not established')
# connect.close()


# import cx_Oracle
# try:
#     #query = "Create table employees(eno number,ename varchar(20),esal number(10,2),eaddr varchar2(10));"
#     query = "insert into employees values(:eno,:ename,:esal,:eaddr);"
#     con = cx_Oracle.connect('scott/tiger@localhost')
#     cursor = con.cursor()
#     records = [(200,'vani', 2000, 'Tirupati'), (400,'kavya', 5000, 'Chennai'), (600,'Chaturvi', 7000, 'Bangalore')]
#     #cursor.execute(query)
#     cursor.executemany(query,records)
#     #print('Table created succesfully')
#     print('Records inserted successfully')
# except cx_Oracle.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('There is problem: ',a)
# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()



# import cx_Oracle
# try:
#
#     query ="insert into Employees values(%d,%s,%f,%s);"
#     con = cx_Oracle.connect('scott/tiger@localhost')
#     cursor = con.cursor()
#     while True:
#         eno = int(input('Enter the Employee number: '))
#         ename = input('Enter the Employee name: ')
#         esal = float(input('Enter Employee salary: '))
#         eaddr = input('Enter Employee Address: ')
#         cursor.execute(query %(eno,ename,esal,eaddr))
#         con.commit()
#         #print('Record inserted successfully')
#         option = input('Do you want to insert one more record[yes][no]')
#         if option == 'no':
#             break
#     print('All Records inserted successfully')
# except cx_Oracle.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('There is problem: ',e)
# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()



# import cx_Oracle
# try:
#     con=cx_Oracle.connect('scott/tiger@localhost')
#     cursor=con.cursor()
#     increment=float(input('Enter increment salary: '))
#     salrange=float(input('Enter salary range: '))
#     query="update Employees set esal = esal+%f where esal<%f;"
#     cursor.execute(query %(increment,salrange))
#     print('Records updated successfully')
#
# except cx_Oracle.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('There is problem: ',e)
# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()



# import cx_Oracle
# try:
#     con=cx_Oracle.connect('scott/tiger@localhost')
#     cursor=con.cursor()
#     cutoff=float(input('Enter cutoff salary: '))
#     query="delete from Employees where esal>%f"
#     cursor.execute(query %cutoff)
#     con.commit()
#     print('Records deleted successfully')
#
# except cx_Oracle.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('There is problem: ',e)
# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()



# import cx_Oracle
# try:
#     con=cx_Oracle.connect('scott/tiger@localhost')
#     cursor=con.cursor()
#     query="select * from employees"
#     cursor.execute(query)
#     row=cursor.fetchone()
#     while row is not None:
#         print(row)
#         row = cursor.fetchone()
#
# except cx_Oracle.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('There is problem: ',e)
# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()


# import cx_Oracle
# try:
#     con=cx_Oracle.connect('scott/tiger@localhost')
#     cursor=con.cursor()
#     query="select * from employees"
#     cursor.execute(query)
#     data=cursor.fetchall()
#     print(data)#list of tuples
#     for row in data:
#         print('Employee Number: ',row[0])
#         print('Employee Name: ',row[1])
#         print('Employee sal: ', row[2])
#         print('Employee addr: ', row[3])
#         print()
#
# except cx_Oracle.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('There is problem: ',e)
# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()


# import cx_Oracle
# try:
#     con=cx_Oracle.connect('scott/tiger@localhost')
#     cursor=con.cursor()
#     query="select * from employees"
#     n=int(input('Enter the number of required rows: '))
#     cursor.execute(query)
#     data=cursor.fetchmany(n)
#     print(data)#list of tuples
#     for row in data:
#         print('Employee Number: ',row[0])
#         print('Employee Name: ',row[1])
#         print('Employee sal: ', row[2])
#         print('Employee addr: ', row[3])
#         print()
#
# except cx_Oracle.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('There is problem: ',e)
# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()



import cx_Oracle
try:
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    query="select * from employees"
    n=int(input('Enter the number of required rows: '))
    cursor.execute(query)
    data=cursor.fetchmany(n)
    f = open('file.txt','w')
    f.write(str(data))

except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('There is problem: ',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()




































































