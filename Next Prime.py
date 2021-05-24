n=int(input("Enter the number"))
count=0
n+=1
while count==0:
    for i in range(2,n,1):
        if n%i==0:
            n+=1
    else:
            print(n)
            count+=1
        
