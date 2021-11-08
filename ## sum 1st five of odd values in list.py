## Please use this space to test and run your code
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
count = 0
sums = 0
for num in num_list :
    if count >5 :
        break
    if num%2 ==1 :
        count +=1
        sums += num
        print(count,sums)
    
print(sums)