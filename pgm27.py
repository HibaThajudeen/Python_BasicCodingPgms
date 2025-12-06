x=input("Enter Number: ")
lst=["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
for i in x:
    if i=="-":
        print("Minus", end=" ")
    else:
        print(lst[int(i)], end=" ")