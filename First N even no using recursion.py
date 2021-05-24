def even(n):
    if n>0:
        even(n-1)
        print(2*n)
n=int(input("Enter The N number"))
even(n)
        
        
