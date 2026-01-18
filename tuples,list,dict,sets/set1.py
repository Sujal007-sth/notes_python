#set
#no repetation
#sets are unordered 
#cannot change existing values
#not indexed (no 0123)

a = {1,34,23,45}#set
b = {}#empty dictionary
a1 = set()#empty set
print(a1) 
#methods of sets
s = {1,2,"sujal"}
print(s, type)
#add
s.add("new added")
print(s)
print(len(s))
s.remove("sujal")
remove = s.pop()#removes random item
print(s,remove)
#union and intersection 
s1 = {1,2,3}
s2 = {3,4,5}
print(s1.union(s2))#every values with no rep
print(s1.intersection(s2))#common values

