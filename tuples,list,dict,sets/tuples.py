#tupels are not mutable unlike list
a = (1,2,3,4, True, "sujal")
b = ()#empty tuple
c = (1,)#tuple with one element
d = (1)
print(type(a))
print(type(c))
print(type(d))

#methods of tuples
a1 = (1,2,2,3,4,"sujal")
no = a1.count(2)
print(no)
