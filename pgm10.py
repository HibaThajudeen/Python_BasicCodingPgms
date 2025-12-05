x = int(input("Enter Number: "))
n= x
r= 0
print("Reversed Number: ", end="")
while x != 0:
    l= x%10
    r= r*10 +l
    x= x//10
print(r)
if n==r:
    print("Palindrome")
else:
    print("Not Palindrome")