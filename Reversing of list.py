def reverse(no):
    new_lst= no[::-1]
    return new_lst

no= list(input("Enter The Number").split())
ele= reverse(no)
print(ele)