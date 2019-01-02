result = 0
out = None

while out != 0:

    def var_input_for_numbers(value):
        if isinstance(value, str):
            while True:
                try:
                    i = float(input("{}".format(value)))
                    return i
                except Exception as e:
                    print("Error: you must use only numbers, ", e)
        else:
            raise Exception("Please integer")



    def var_input_for_op(value):
        valid_operation = ['+', '-', '/', '*', '//', '%']
        if isinstance(value, str):
            while True:
                try:
                    s = input("{}".format(value))
                    if s in valid_operation:
                        return s
                except Exception as e:
                    print("Error: {} ", e)
        else:
            raise Exception("Please string")




    first_checked_value = var_input_for_numbers("Enter first number: ")
    second_checked_value = var_input_for_numbers("Enter second number: ")
    op_checked_value = var_input_for_op("operation: ")





    #valid_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


    def division_check(first_number, second_number, operation):

        try:
            if operation == "/":
                result = first_number / second_number
                print(result)
            elif operation == "//":
                result = first_number // second_number
                print(result)
            elif operation == "%":
                result = first_number % second_number
                print(result)
        except ZeroDivisionError as zde:
            print("Error: ", zde)
        except Exception as e:
            print("Error: ", e)

    division_check(first_checked_value, second_checked_value, op_checked_value)


    def calculator_main(first_number, second_number, operation):
        try:
            if operation == "+":
                result = first_number + second_number
                print(result)
            elif operation == "-":
                result = first_number - second_number
                print(result)
            elif operation == "*":
                result = first_number * second_number
                print(result)
            else:
                return False
        except Exception as e:
            print("Error: ", e)

    calculator_main(first_checked_value, second_checked_value, op_checked_value)

    out = int(input("Enter '1' to continue. Otherwise enter 0 to exit: "))
