class Myfam:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role
    def status(self):
        print('they are happy')
    def yolo(self, x):
        self.friends = x
        notj = x+2
        return notj
f1 = Myfam('sujal','18', 'son')

print(f1.name)
print(Myfam.__doc__)
#everything is obj in python



