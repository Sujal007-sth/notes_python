a = "sujal"
b = "shrestha"
c = '''s s 
       s  s'''
print(c)
#string slicing = for getting parts of string
#strings are immutable, once its made it cannot change(existing string cannot be changed)
ashort = len(a) #printing length
ahort = a[0:1]
d = b[4:5]
# print(d)

# print(ashort)
# print(ahort) 

#negative slicing
name = "sujal"
print(name[-2:-5])
print(name[:2])#means 0:2
print(name[2:])#means 2:len
print(name[2:4]) 
#skip value
word = "amazing"
print(word[1:7:3])