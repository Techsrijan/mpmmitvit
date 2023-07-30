h,m,e,c,s=100,90,60,86,50
total=h+m+e+c+s
print("total marks=",total)
per=(total*100)/500
print("percentage=",per,"%")
if per<33:
    print("you are fail")
elif per>=33 and per<45:
    print("third division")
elif per>=45 and per<60:
    print("second")
elif per>=60:
    print("First")
    


