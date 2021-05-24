def nat(N):
    if N==1:
        return N
    else:
        return N+nat(N-1)
N=int(input("Enter the N no "))
s=nat(N)
print("Sum is- ",s)
