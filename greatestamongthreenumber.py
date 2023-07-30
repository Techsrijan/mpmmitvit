a=int(input("enter the first number"))
b=int(input("enter the Second number"))
c=int(input("enter the third number"))

if a>b:
    if a>c:
        print("a is greatest")
    else:
        print("c is greatest")
elif b>c:
    print("b is greatest")
else:
    print("c is greatest")

