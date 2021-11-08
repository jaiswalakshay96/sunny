# Take in the Marks of 5 Subjects and Display the Grade

a = []
c=[]
for i in range(5):
    b=input('enter marks (0 - 100) in subject {} : '.format(i))
    a.append(int(b))

for i in range(5):
    if (a[i] >= 80):
        gra= 'A'
    elif a[i] >=60 and a[i]<80:
        gra = 'B'
    elif a[i] >=50 and a[i]<60:
        gra = 'C'
    elif a[i] >=60 and a[i]<80:
        gra = 'D'
    else :
        gra = 'F'
    c.append(gra)
print (c)

for i in range(5):
    print(a[i] , c[i])