def check_prime(num):
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count = count+1
    if count ==2:
        return "is a prime number"
    else:
        return "is not a prime number"
x = int(input("enter a number: "))
res = check_prime(x)
print(res)
count = 1#count inside the fn and this count are diff
print(count)




