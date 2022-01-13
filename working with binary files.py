import pickle
b=open("lotsofdata.dat", 'ab+')
stu={}
a='y'
while a=='y':
    roll=int(input("enter roll number"))
    name=input("enter name")
    age=input("enter age")
    marks=input("enter marks")
    stu['Roll no.']=roll
    stu['Name']=name
    stu['Age']= age
    stu['marks']= marks
    pickle.dump(stu, b)
    a=input("wanna go again? y/n")
b.seek(0)
try:
    while True:
        p=pickle.load(b)
        print(p)
except:
    b.close()
