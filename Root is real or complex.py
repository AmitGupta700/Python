a=int(input("Enter the number"))
b=int(input("Enter the number"))
c=complex(a,b)
print(c)
if c.real>c.imag:
    print("Real part is greater than imaginary part")
elif c.real==c.imag:
    print("Both are equal")
else:
    print("Imaginary part is greater")
