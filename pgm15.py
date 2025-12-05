x= input("Enter String: ")
for i in set(x):
    if x.count(i)==1:
        print(i, x.count(i))