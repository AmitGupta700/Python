def merge(dict1, dict2):
    return(dict2.update(dict1))

dict1= {'R': 'Red', 'B': 'Black', 'P':'Pink'}
dict2= {'G': 'Green', 'W': 'White'}

print(merge(dict1, dict2))
print(dict2)