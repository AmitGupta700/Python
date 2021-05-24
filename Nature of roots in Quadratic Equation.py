a=int(input("Enter the number a: "))
b=int(input("Enter the number b: "))
c=int(input("Enter the number c: "))
d=b**2-4*a*c
if d>0:
    print("Roots are real and different")
elif d==0:
    print("Roots are real and equal")
elif d<0:
    print("Roots are complex")
