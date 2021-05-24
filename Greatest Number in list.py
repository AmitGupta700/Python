l=[int(e) for e in input("Enter the number seperated by comma").split(",")]
max=l[0]
for x in l:
    if x>max:
        max=x
print(max)
