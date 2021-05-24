num=int(input("Enter the no of N prime no you want"))
l=[]
count=0
x=1
while count<num:
    for i in range(2,x):
         if x%i==0:
            x+=1
    else:
      l.append(x)
      count+=1
      x+=1
print(l)
