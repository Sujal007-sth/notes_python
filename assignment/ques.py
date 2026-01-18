#find the 2nd largest number 
num = [1,23,3,4,5,6] 
print(num)
def largest(numm):
    great = 0
    for x in numm:
        if great < x:
            great = x
    return great

largeNum = largest(num)

num.remove(largeNum)
print(num)
final = largest(num)
print(f"second largest number {final}")

