#print only consonants
x = input("Enter String: ").lower()
for i in x:
    if i not in "aeiou":
        print(i, end=" ")