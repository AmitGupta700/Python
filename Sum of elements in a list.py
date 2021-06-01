n = int(input("Enter the size of list : "))
print("\n")
numList = list(map(float, input("Enter the list numbers separated by space ").strip().split()))[:n]
print("User List: ", numList)
total=0
for i in range(0,len(numList)):
    total=total + numList[i]
print(total)