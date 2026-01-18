#constructer= init function (executes when an object is created )
#all classes have a init func, which is always executed when an obj is created
class Student:
    
    def __init__(self):
        print(self)#self is always latest parameter (in this it is s1)
        print('adding new student in database')
    


#creating obj (instance)
s1 = Student()#when s1 is created init func is automatically called,() is put to call the constructer(init)
#constructer always takes an argument/parameter called self parameter


class Car:

    def __init__(self, make, model, year):#it triggers automatically after obj is made
        self.make = make #atributes of obj
        self.model = model
        self.year = year

    def drive(self):#slef is called the obj we are currently making/using it
        print('hi')
    def stop(self):
        print('everyone')

car1 = Car('honda', 'corvet',2021)
print(car1.make)
print(car1)
car1.drive()#going to drive func
car2 = Car('suv', 'skjf', 1990)#currently car2 is self, suv is passed in model and car2 is passed to self
print(car2.model)






class Football:
    def __init__(self,name,age,height,club):
        self.name = name 
        self.age = age
        self.height = height
        self.club = club
    def award(self):
        print('ballon dor')  
p1 = Football('neymar',34,1.75,'santos')
print(p1.name)
print(p1.club)
print(p1.height)
p1.award()

class address:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
#self always represents current object


class car():
    def __init__(self):
        self.speed = 0
    def accelerate(self):
        self.speed += 5
    def brake(self):
        self.brake -= 5
    def display(self):
        print()