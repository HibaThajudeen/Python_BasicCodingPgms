def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
x= int(input("Enter a number: "))
for i in range(x+1):
    print(fib(i))