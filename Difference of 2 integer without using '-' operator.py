#WAP to find diffrence of two small integers without using minus(-) operator.
a=int(input("Enter The First Number"))
b=int(input("Enter The Second Number"))
sub=a+(~b)+1
print("Substraction of %d-%d=%d"%(a,b,sub))
input("Press ENTER to exit")
