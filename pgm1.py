x = int(input("Enter a number "))
if x%2 != 0:
    print("Weird")
elif x%2 == 0 and x>=2 and x<=5:
    print("Not Weird")
elif x%2 == 1 and x>=6 and x<=20:
    print("Weird")
elif x%2 == 0 and x>20:
    print("Not Weird")