#use for loop when you know how many times you need to repeat something
for i in range(1,100+1):
    print(i,end=" ")

#while loop
#runs only when condtion is true
#while using while make it such that it makes the condtion false 
i = 1
while i < 6:
    print("hi")
    i = i+1

# i = 1 
# while i<51:
#     print(i)

lis = [1,2,3,4]
i = 0 #we put i = 0 because of indexing if we put 1 then lis[1] = 2 we would miss 0 index (1)
while i<len(lis):
    print(lis[i])
    i = i+1


l = [1,2,3,4,5,6,7,8]
for i in l:
    print(i)

#range (start, stop, step-size)

#for loop with else
eg =[1,2,3]
for i in eg:
    print(eg)
else:
    print("done")# prints when the loop exhausts
