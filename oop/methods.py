#methods = functions that belongs to obj
#normal methods

class Student:
    def __init__(self,name, address):
        self.name = name
        self.address = address
    #methods 
    def hello(self):
        print("hello", self.name)
    
    def address(self):
        return self.address
    
s1 = Student("sujal", "hattiban")
print(s1.name)
s1.hello()
print(s1.address())