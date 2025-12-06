import math
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
c=int(input("Enter value of c: "))
d=b**2-4*a*c
if d>0:
    x1=(-b+math.sqrt(d))/(2*a)
    print("x1=",x1)
    x2=(-b-math.sqrt(d))/(2*a)
    print("x2=",x2)
elif d==0:
    x1=(-b/(2*a))
    print("x1=",x1)
    x2=(-b/(2*a))
    print("x2=",x2)
elif d<0:
    print("No real root")

