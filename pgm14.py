x= input("Enter String: ")
r= x[::-1]
print("Reversed String: ",x[::-1])
if x.lower()==r.lower():
    print("Palindrome")
else:
    print("Not Palindrome")