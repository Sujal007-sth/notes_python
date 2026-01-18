#conatiner to store data of any type
friends = ['sujal','swopnil','sameer',1,2,3,True]
print(friends[0])
#in list the the index starts from 0 from backwards -1
# eg freinds = ['sujal'(index 0),'swopnil'(index1)]
friends[0]= False #changing data
print(friends)
#lists are mutable or changable
#string cannot be changed 
#list can be changed
friends.append(12)#adds at the end 
print(friends)
#sorting = puts in ascending order
l1 = [1,12,3,5,6,7,8,2,11]
l1.sort()
print(l1)
#reverse
l1.reverse()
print(l1)
#insert = to add/put at the particulat index
l1.insert(3, 'what you want add at index 3')
print(l1)
#pop = will delete ann element of particular index

