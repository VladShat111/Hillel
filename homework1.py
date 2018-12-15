a = input("Enter first number or string: ")
b = input("Enter second number or string: ")
c = input("Enter action symbol: ")


def calculator(x, y, z):

    try:
        if z == "+":
            if x and y in "0123456789":
                print(int(x) + int(y))
            else:
                print(x + y)
        elif z == "-":
            print(int(x) - int(y))
        elif z == "*":
            print(int(x) * int(y))
        elif z == "/":
            print(int(x) / int(y))
        elif z == "//":
            print(int(x) // int(y))
        elif z == "%":
            print(int(x % y))
        else:
            return None
    except ZeroDivisionError:
        print("Error: Go to school :)")

calculator(a, b, c)




