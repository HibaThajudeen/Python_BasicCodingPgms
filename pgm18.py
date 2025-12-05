#Slicing
lst = ["apple",55,77,33,21,8]
print(lst[::-1])

#Positive Indexing
lst = ["apple",55,77,33,21,8]
for i in range(len(lst),0,-1):
    print(lst[i-1],end=" ")

#Negatvie Indexing
lst = ["apple",55,77,33,21,8]
for i in range(-1,-len(lst)-1,-1):
    print(lst[i],end=" ")