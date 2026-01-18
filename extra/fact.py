def fact(para):
    factorial = 1
    for i in range(1, para+1):
        factorial *= i
    return factorial

while True:
    try: 
        num1 = int(input('Enter your first number: '))
        num2 = int(input('Enter your second number: '))
    except ValueError:
        print('Pleae enter only integer')
    else:
        break
    
sub = fact(num1) - fact(num2)
print(f'answer is {sub}')

