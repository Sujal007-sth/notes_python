try:
    print(10/0)
except IndexError:
    print("index error")
except ZeroDivisionError:
    print("zero division error")
except BaseException:
    print("error")
#finally get program executed (exception aayena vane pani it executes )
