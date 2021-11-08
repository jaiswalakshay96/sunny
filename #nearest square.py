limit = float(input('enter no :'))
nearest_square = 'Invalid'
# write your while loop here
x =(limit)
y = 2
while 1 < x <= limit :
    while 2 < y <=limit//2 :
        #print (y)
        if (x%(y**2) == 0) :
            nearest_square = x
    y += 1
x -=1
print(x,y)
print(nearest_square)