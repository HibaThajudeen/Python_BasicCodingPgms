num= int(input("Enter a number: "))
ans=0
x=num
a=len(str(num))
while x!=0 :
    ans=ans+((x%10)**a)
    x=x//10
if ans==num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")