class Car:
    #default constructors
    def __init__(self):
        print("defualt constructor")
    def __init__(self,model,weight):
        self.x = model#new variable is created in class
        self.weight = weight
c1 = Car("Bmw", 5000)
print(c1.x,c1.weight) #print in same line

#for car2
c2 = Car("honda", 600000) 
print(c2.x)
print(c2.weight)  
