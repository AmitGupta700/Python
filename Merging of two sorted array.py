t=eval(input("Enter the tuple"))
t2=eval(input("Enter the tuple"))
l=list(t)
l.sort()
t1=tuple(l)
print(t1)
l1=list(t2)
l1.sort()
t3=tuple(l1)
print(t3)
t4=t1+t3
print(t4)

