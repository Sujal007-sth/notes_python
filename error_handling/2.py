# try: 
#     a = int(input("enter a number: "))
# except ZeroDivisionError:
#     print("zero division error")
# except ValueError:
#     print("that is not a valid number")
# except BaseException:
#     print("error")
# finally:
#     print('I dont care about the error')

class MyError(Exception):
    pass

try: 
    print(10/0)
    raise MyError("this is my error!")
except MyError as e:
    print("Custom error",e)
    





