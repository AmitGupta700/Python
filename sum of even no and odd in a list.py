l=[int(e) for e in input("Enter the number seperated by comma").split(",")]
evensum=0
oddsum=0
for x in l:
    if x%2==0:
        evensum+=x
    else:
        oddsum+=x
print("Sum of even no is: ",evensum)
print("Sum of odd no is: ",oddsum)
