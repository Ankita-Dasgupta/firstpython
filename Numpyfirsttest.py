def increment(marks):
    p=[]
    for m in marks:
        m = m + 5
        if (m>100):
            m=100
        p.append(m)
    return p
def decrement(marks):
    for i in range(0,len(marks)):
        marks[i] = marks[i] - 5
        if (marks[i]<0):
            marks[i]=0
a = [45,55,96,85]
a = increment(a)
print(a)
decrement(a)
print(a)
