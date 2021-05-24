x=int(input("Enter The 1 Number: "))
y=int(input("Enter The 2 Number: "))
z=int(input("Enter The 3 Number: "))
if x>y:
    if x>z:
        print("%d is Greatest number" %x)
    else:
        print("%d is greatest number" %z)
elif x<y:
    if y>z:
        print("%d is greatest number" %y)
    else:
     print("%d is greatest number" %z)
