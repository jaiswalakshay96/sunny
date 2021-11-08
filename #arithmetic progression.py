#arithmetic progression
a = int(input("enter a "))
b = int(input("enter b "))
n = int(input("enter n "))

 
d = (b - a)
t = b
l = [a,b]
for i in range(n - 2) :
    t = t + d
    l.append(t)
print(t)
print(l)