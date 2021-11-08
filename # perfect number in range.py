# perfect number in range

a = int(input("enter a : "))
b = int(input("eneter b : "))
p = []

for n in range(a,b+1) :
    sums = 0  ############### MOST IMPORTANT STEP, SUM ==0 INSIDE FIRST LOOP
    for x in range(1,n) :
        if n % x == 0 :
            sums += x
    
    if sums == n :
        p.append(sums)
print(p)    