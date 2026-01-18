with open("sujal.txt", "r") as f1:
    data = f1.read()

with open("shrestha.txt", "w") as f2:
    f2.write(data)

print("Content copied successfully!")
