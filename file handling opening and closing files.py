#creating a file
file1= open("fs_overview.txt", "w+")
file1.write("This is a course on forensic science.\n")
file1.write("It is taught by University of Singapore.\n")
file1.write("This is a 4 week course with 2 week deadlines.\n")
file1.write("The father of forensic science is Edmond Locard.\n")
file1.seek(0)
a=' '
b=' '
tot=0
size=0
while b:
    b=file1.readline()
    tot=tot+len(b)
    size=size+len(b.strip())
print("total size= without EOL", tot)
print("size=", size)
'''
while a:
 a=file1.readline()#.strip(" ")
 print(a, end='')
file1.seek(0)
for i in file1:
    print(i)
'''

file1.close()