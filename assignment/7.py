lis = []
for i in range(5):
    lis.append(input("enter cities: "))
lis.sort()
print(lis)

for k in lis:
    
    if k.startswith("k"):
        print(k)
lis.append("kathmandu")
print(lis)
    