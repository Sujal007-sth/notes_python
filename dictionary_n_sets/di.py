def fact(val):
    factorial = 1
    for i in range(1, val+1):
        factorial *= i
    return factorial
num_one = 7
num_two = 5
result = fact(num_one) - fact(num_two)
print(f'difference is {result}')

