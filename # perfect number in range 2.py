# perfect number in range
#a = int(input("enter a : "))
#b = int(input("eneter b : "))
n = 30

p = []
sums = 0
for x in range(1,n) :
    if n % x == 0 :
        sums += x
if sums == n :
    print('{} is perfect no'.format(n))
else:
    print('{} is not perfect no'.format(n))