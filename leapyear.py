year=int(input("enter any year"))
print(year)
if year%100==0:
    if year%400==0:
        print("Leap year")
    else:
        print("Not Leap year")
elif year%4==0:
    print("Leap year")
else:
    print("not leap")