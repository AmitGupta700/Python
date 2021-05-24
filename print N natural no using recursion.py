def naturalno(n):
    if n>0:
        naturalno(n-1)
        print(n)
naturalno(int(input()))
