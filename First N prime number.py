n=int(input("Enter the number"))
x=1
count=0
while count<n:
    for d in range(2,x,1):
        if x%d==0:
            x+=1
    else:
        print(x)
        x+=1
        count+=1

        
