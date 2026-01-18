#dictionary 
#unordered, mutable, indexed()
#keys should be unique but values should be same
#if theres 2 same keys in the dict python will keep the last one, and overwrites the previous value
marks = {
    "sujal": 100,#keys: value
    "harry": 50,
    "list": [1,2,3]
}
print(marks["sujal"])
print(marks["list"])


#methods of dictionry
print(marks.items())#gives items(keys and values) in the form of tuples 
print(marks.keys())
print(marks.values())
marks.update({"sujal": 10, "ram": 190})#updating dict cuz dict is mutable and we can add in it too
print(marks)
print(marks.get("sujal"))#gives vlaues of the key 
#diff between get method and normal
#print(marks.get("sujal12"))#since there no sujal12 it gives none
#print(marks["sujal12"])#gives key error
copied = marks.copy()
print(copied)
#different keys but same value
keys = ["a","b"]
dicto = dict.fromkeys(keys,1)# from keys list, value
print(dicto)