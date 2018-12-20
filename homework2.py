Exit = None
while Exit != 0:
    a = input("Enter first number or string: ")
    b = input("Enter second number or string: ")
    c = input("Enter operation: ")

    valid_operation = "+-/*//%"

    if c not in valid_operation:
        print("Error. Invalid symbol")


    def calculator(x, y, z):
        try:
            if z == "+":
                if x and y in "0123456789":
                    print(int(x) + int(y))
                else:
                    print(x + y)
            elif z == "-":
                print(float(x) - float(y))
            elif z == "*":
                print(float(x) * float(y))
            elif z == "/":
                print(float(x) / float(y))
            elif z == "//":
                print(float(x) // float(y))
            elif z == "%":
                print(float(x) % float(y))
            else:
                return False
        except ZeroDivisionError:
            print("Error: Go to school :) _zero_division_")
        except ValueError:
            print("Error. Check your entering value  For string you can only use '+' operation.")


    calculator(a, b, c)
    Exit = int(input("Enter '1' to continue. Otherwise enter 0 to exit: "))
