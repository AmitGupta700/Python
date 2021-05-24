t=eval(input("Enter the tuple"))
l=list(t)
l1=[]
l2=[]
l3=[]
for x in l:
    if type(x)==int:
        l1.append(x)
    elif type(x)==float:
        l2.append(x)
    else:
        l3.append(x)
t1=tuple(l1)
t2=tuple(l2)
t3=tuple(l3)
print(t1)
print(t2)
print(t3)
        
        

        
        
