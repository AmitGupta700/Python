n=int(input("Enter The n prime no: "))
count=0
i=1
l=[]
while count<n:
    for d in range(2,i,1):
         if i%d==0:
            i+=1
    else:
        l.append(i)
        i+=1
        count+=1
s=set(l)
print(s)
