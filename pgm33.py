x=input("Enter string:")
stack=[]
flag=0
key={")":"(","}":"{","]":"["}
for i in x:
    if i in "({[":
        stack.append(i)
    else:
        if not stack or key[i] != stack[-1]:
            flag=1
            break
        stack.pop()

if flag==0:
    print("The string is valid")
else:
    print("The string is not valid")
