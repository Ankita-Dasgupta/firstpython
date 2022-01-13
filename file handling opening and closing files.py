#creating a file
file1= open("fs_overview.txt", "a+")
line=" "
file1.seek(0)
'''
v=0
c=0
while line:
    line=file1.read(1)
    for i in line.split():
        if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            v=v+1
            print(i)
        else:
            c=c+1
print("c=", c)
print("v=", v)
'''
'''
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
'''
c=0
'''
a= ' '
while a:
    a=file1.readline()#.strip()
    print(a, end='')


'''
for i in file1:
    print(i)
'''
'''
a=file1.readlines()
count=len(a)
print(a, count)
'''
file1.flush()
file1.close()