def cube(n):
    if n>0:
        cube(n-1)
        print(n**3)
n=int(input("Enter The N number"))
cube(n)
        
        
