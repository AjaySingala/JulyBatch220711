# a file named "test.txt", will be opened with the reading mode.
file = open('test.txt', 'r')
#This will print every line one by one in the file
for each in file:
    print (each)

# Python code to create a file
file = open('test.txt','w')
file.write("This is the write command\n")
file.write("It allows us to write in a particular file\n")
file.close()

# Python code to illustrate read() mode
file = open("test.txt", "r") 
print (file.read())

# Python code to illustrate read() mode character wise
file = open("test.txt", "r")
print (file.read(10))
print((file.read(20)))
print(file.read(25))

f=open("test.txt", "r")
if f.mode == 'r':
    contents = f.read()
    print(contents)
print(f.mode)
f.close()

f=open("test.txt", "r")
lines = f.readlines()
print(type(lines))
for line in lines:
    print(line)
f.close()

f = open("test2.txt","w+")
for i in range(10):
    f.write("This is line %d\r\n" % (i+1))
f.close() 

# Python code to illustrate append() mode
file = open('test.txt','a')
file.write("This will add this line\n")
for i in range(10):
    file.write("This is line %d\r\n" % (i+1))
file.close()

# # Python code to illustrate with() alongwith write()
with open("file.txt", "w") as f: 
    f.write("Hello World!!!\n")
    for i in range(3):
        f.write("Line #:" + str(i) + "\n")

# Python code to illustrate split() function
with open("test.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)

with open("file.csv", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split(",")
        print (word)
