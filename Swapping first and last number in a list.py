def swapping(no):
    for i in no:
        size= len(no)
        temp=no[0]
        no[0]=no[size-1]
        no[size-1]=temp
        return no

no= list(input("Enter The Number").split())
ele= swapping(no)
print(ele)