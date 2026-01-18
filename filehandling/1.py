fwrite = open("/Users/sujal/Documents/python/filehandling/2.py","w")
fwrite.write("hi welcome to the world")
fwrite.close()
dict = {

}
import json

data = {"name": "Sujal", "age": 20, "city": "Kathmandu"}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
