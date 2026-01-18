#ordered
lis1 = ["sujal","shrestha", 5, "harry", True]
print(lis1[0])
lis1[0] = "man"#changing value of index 0, unlike string list is mutable(changable)
print(lis1[0])
print(lis1)#new list
#list slicing
print(lis1[0:3])

#methods of list to change the list
lis2 = ["sujal",7,9]
lis2[1] = 6#changing 2nd item from list
print(lis2) #unlike string list is changed and not some new value is made
lis2.append(10)#adding 10 at the end
print(lis2)
lis2.reverse()
print(lis2)
lis2.insert(2,"shrestha") #insert shrestha such that its index in the list is 2
print(lis2)
lis2.pop(3)#remove the value at index 3
