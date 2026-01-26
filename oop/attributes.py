#two types of attributes 
#class.attr = attributs which are common for every obj
#obj.attr = which is different for every object
#self.name = harek obj ko name diff hunxa
#common kura lai ek choti matra store garxa = class attribute
#eg = name of the college
class Student:
    college_name = "The british College" #class attr as same for every stud and stored only once in the memory
    def __init__(self,name):
        self.name = name
s1 = Student("sujal")
print(s1.name)
print(s1.college_name)
print(Student.college_name) 