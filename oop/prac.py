class Student:
    def __init__(self,name,eng,nep,comp):
        self.name = name
        self.eng = eng
        self.nep = nep 
        self.comp = comp

    def average(self):
        avg = (self.eng + self.nep + self.comp) / 3
        return avg
    
s1 = Student("sujal", 90,89,88)
print(s1.name, s1.eng, s1.nep, s1.comp)

print(s1.average())

#by using list and loop

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        sum = 0
        for i in self.marks:
            sum = sum + i
        return ("the average is", sum/3)


s1 = Student("sujal", [89,98,90])

print(s1.average())
