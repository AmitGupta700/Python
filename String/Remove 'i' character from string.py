str=input("Enter The string")
print(str)
i=int(input("Enter The position you want to remove"))
new_str= str[:i]+str[i+1:]
print(new_str)