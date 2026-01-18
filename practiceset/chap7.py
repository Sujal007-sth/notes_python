# #print mul table of a number
# n = int(input("enter a number: "))
# print(f'Multiplication table of {n}')

# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")

#write a program to greet all the person starting with 'l' and which starts with 's' in a list

l = ["Harry","Sohan", "Sachin", "Rahul"]
for i in l:
    if i.startswith("S"):
        print(f"good morning {i}")


    
#do qn 1 with while loop
n = int(input("number: "))
i = 1
while i<11:
    print(f" {n} X {i} = {n*i}")
    i = i+1

#sum of first 10 natural numbers
# n = int(input("enter: "))
# i = 0
# while i<n :
#     sum = sum+i
#     i = i+1

#find the factorial 
# eg 5! = 1 X 2 X 3 X 4 X 5
def factorial(n):
    product = 1
    for i in range(1,n+1):
        product = product * i 
    return(f"the factorial of {n} is {product}")
x = int(input("enter a number: "))
result = factorial(x)
print(result)