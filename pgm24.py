x=int(input("Enter a number: "))
sq=x**2
n=len(str(x))
if sq%(10**n)==x:
    print("Automorphic")
else:
    print("Not Automorphic")