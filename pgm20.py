x= int(input("Enter Year: "))
if x%4==0:
    if x%100==0:
        if x%400==0:
            print("It is a leap year")
        else:
            print("Not a leap year")
    else:
        print("It is a leap year")
else:
    print("Not a leap year")