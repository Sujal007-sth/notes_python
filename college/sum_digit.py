
def sum_digit(num):
    sum = 0
    while num != 0:
     
     rem = num%10
     sum = sum+rem
     num = num//10
    return sum
num = int(input('enter a number:'))

result = sum_digit(num)

print(result)
