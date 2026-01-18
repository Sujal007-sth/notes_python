def add(*x):
    summ = 0
    for i in  x:
        summ += i
    return summ

print(add(10, 20, 30, 40, 50))


def sub(**x):
    print(x)

sub(x = 20, y = 200)


def setup():
    print("second")
    def live():
        print("first")
    return live

setup()()