from collections import Counter

dict= {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
k = Counter(dict)
  
# Finding 3 highest values
high = k.most_common(3) 
  
print("Initial Dictionary:")
print(dict, "\n")
  
  
print("Dictionary with 3 highest values:")
print("Keys: Values")
  
for i in high:
    print(i[0]," :",i[1]," ")