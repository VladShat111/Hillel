result = 0

out = None
while out != 0:
    a = input("Enter first number or string: ")
    b = input("Enter second number or string: ")
    c = input("Enter operation: ")

    valid_operation = ['+', '-', '/', '*', '//', '%']

    valid_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if c not in valid_operation:
        print("Error. Invalid operation")


    def calculator(first_number_or_string, second_number_or_string, operation):
        try:
            if operation == "+":
                if first_number_or_string and second_number_or_string in valid_numbers:
                    result = int(first_number_or_string) + int(second_number_or_string)
                    print(result)
                else:
                    result = first_number_or_string + second_number_or_string
                    print(result)

            elif operation == "-":
                result = float(first_number_or_string) - float(second_number_or_string)
                print(result)
            elif operation == "*":
                result = float(first_number_or_string) * float(second_number_or_string)
                print(result)
            elif operation == "/":
                result = float(first_number_or_string) / float(second_number_or_string)
                print(result)
            elif operation == "//":
                result = float(first_number_or_string) // float(second_number_or_string)
                print(result)
            elif operation == "%":
                result = float(first_number_or_string) % float(second_number_or_string)
                print(result)
            else:
                return False
        except ZeroDivisionError:
            print("Error: Go to school :) _zero_division_")
        except ValueError:
            print("Error. Check your entering value  For string you can only use '+' operation.")
        except Exception as e:
            print("Error: ", e)


    calculator(a, b, c)

    out = int(input("Enter '1' to continue. Otherwise enter 0 to exit: "))



