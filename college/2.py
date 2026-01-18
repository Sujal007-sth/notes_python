# def smallest_value(a,b):
#     if a>b:
#         return "b is smallest"
#     else :
#         return"a is smallest"
# a = int(input("enter a number(a): "))
# b = int(input("enter a number(b):"))
# res = smallest_value(a,b)
# print(res)
        
#ex 1,2,3,4(submission due date nov11)

# def cube(num):
#     cube_num = num**3
#     return cube_num
# num = int(input("enter a number: "))
# result = cube(num)
# print(f" cube of  {num} is {result}")

home = input("enter your address: ")
name = input("enter your name: ")
print(f"My name is {name} and I live in {home}")

print("""Hello, is your name "Bwian"?""")
print("""Or is your name 'Woger'?""")
print("""This is a string containing a backslash (\\),
a single quote ('), a double quote (")
and is split across multiple lines""")

print("This is a string containing a backslash (\\),\n"
      "a single quote ('), a double quote (\")\n"
      "and is split across multiple lines")

print("""This is a string containing a backslash (\\),
a single quote ('), a double quote (")
and is split across multiple lines""")

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("Temperature in Celsius is:", celsius)

a = input("Enter first value: ")
b = input("Enter second value: ")
a = float(input("Enter first value: "))
b = float(input("Enter second value: "))

print(f"The value 'a' was {a} and the value 'b' was {b}")
print(f"The sum of 'a' and 'b' is {a + b}")
print(f"The product of 'a' and 'b' is {a * b}")

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))

largest_value = max(a, b, c)
print(f"The largest value is {largest_value}")

def print_header(msg):
    """Prints the provided message after five asterisks"""
    print("*****" + msg)
print_header("Welcome to the Program")





