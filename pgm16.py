x= input("Enter String: ")
for i in x:
    if i.islower():
        print(i.upper(), end="")
    else:
        print(i.lower(), end="")


