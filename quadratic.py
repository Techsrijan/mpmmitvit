from math import *
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
d=b*b-4*a*c
if d==0:
    print('roots are real and equal')
    x1=x2=-b/(2*a)
    print("x1=",x1,"x2=",x2)
elif d>0:
    x1=(-b+sqrt(d))/(2*a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print('roots are real and unequal')
    print("x1=", x1, "x2=", x2)
else:
    print("roots are imaginary")
