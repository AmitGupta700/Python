def square(n):
    if n>0:
        square(n-1)
        print(n**2)
n=int(input("Enter The N number"))
square(n)
        
        
