x = int(input("Enter Number: "))
print("Reversed Number: ", end="")
while x != 0:
    l= x%10
    x= x//10
    print(l, end='')