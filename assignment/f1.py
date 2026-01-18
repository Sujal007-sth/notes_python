# def odd_even(num):
#     if num % 2 == 0:
#         return "even"
    
#     else:
#         return "odd"
# x = int(input("Enter a number: "))
# result = odd_even(x)
# print(f"the entered number is {result} ")


num = int(input('enter number: '))
sum = 0
while num !=0 :
    
    reminder = num % 10
    sum = sum+reminder
    num = num // 10
print(sum)
#