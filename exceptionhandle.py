try:
    print("Fridge is open")
    a = int(input("enter the first number"))
    b = int(input("enter the Second number"))
    div=a/b
    print(div)

except ValueError:
    print("You have not entered a number")
except ArithmeticError:
    print("b can not be zero")
except Exception:
    print("something went wrong")
finally:  # always excecutes
    print("Fridge is close")