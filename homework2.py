Exit = None
while Exit != 0:
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
                print(int(x) % int(y))
            else:
                return None
        except ZeroDivisionError:
            print("Error: Go to school :) _zero_division_")


    calculator(a, b, c)
    Exit = int(input("Enter '1' to continue. Otherwise enter 0 to exit: "))
