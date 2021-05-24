def bin(a):
    l=[]
    while a>0:
        rem=a%2
        l.append(rem)
        a=a//2
    l.reverse()
    print("Binary is ")
    print(l)
bin(int(input("Enter the no. ")))


    
