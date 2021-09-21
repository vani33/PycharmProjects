# file = open("C:\\Users\kothapalli.vanisree\\OneDrive - HCL Technologies Ltd\\Desktop\\Newfile.txt", 'r')
# print(file.read())

# file = open("UpdateFile",'w')
# file.write("Welcome to Update file")
#
# file = open("UpdateFile",'r')
# print(file.read())


# file = open("NewUpdateFile",'x')
# file.write("Welcome to New update file")


file = open("NewUpdateFile",'a')
file.write("Hi")

file = open("NewUpdateFile",'r')
print(file.read())