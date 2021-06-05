def palindrome(str):
    return str == str[::-1]

str=input("Enter The string")
ans= palindrome(str)

if ans:
    print("YES")
else:
    print("NO")