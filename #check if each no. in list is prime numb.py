#check if each no. in list is prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here

for nums in check_prime :
    ## HINT: You can use the modulo operator to find a factor
    result = "{} is prime".format(nums)
    for i in range(2,nums) :
        if nums%i == 0 :
            result = str("{} is not prime, because {} is a factor of".format(nums,i)) + str("{}".format(nums))
            #print(result)
            break
        
    print(result)