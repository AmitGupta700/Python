from operator import length_hint

no= list(input("Enter The Number").split())

print("This List is: " +str(no))

list_len_hint= length_hint(no)
print("Length of list is: " +str(list_len_hint))