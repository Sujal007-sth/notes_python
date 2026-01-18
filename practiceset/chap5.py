#1
dict ={
    "kursi": "chair",
    "chiya": "tea"
}
take =input("enter the word you want to translate")
print(dict.get(take))
print(dict)

#2 input 8 number from user and display only unique numbers
numbers = set()
for i in range(1,8+1):
    n = int(input('enter number: '))
    numbers.add(n)
print(numbers)

#3
s = {18, "18"}
print(s)

#4 what will be the len of a?
#len of a will be 2 instead of 3 as because in python 20 == 20.0 is true
a = set()
a.add(20)
a.add(20.0)
a.add("20")
print(a)

#6 creat an empty dict and add 4 friends and their fav lang
dict = {

}
for i in range(4):
    name = input("enter name: ")
    language = input("enter language: ")
    dict.update({name:language})
print(dict)
    