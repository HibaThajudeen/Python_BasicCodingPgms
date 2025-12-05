#Check if a number is a perfect number
sum=0
x=int(input("Enter a number: "))
for i in range(1,(x//2)+1):
    if x%i==0:
        sum=sum+i
if sum==x:
    print("Perfect Number")
else:
    print("Not Perfect Number")

