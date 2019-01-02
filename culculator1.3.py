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
                    print("Error: ", e)
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
                    print("Error: ", e)
        else:
            raise Exception("Please string")




    first_checked_value = var_input_for_numbers("Enter first number: ")
    second_checked_value = var_input_for_numbers("Enter second number: ")
    op_checked_value = var_input_for_op("operation: ")



    #valid_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



    def calculator(first_number_or_string, second_number_or_string, operation):

        if operation == "+":
            result = first_number_or_string + second_number_or_string
            print(result)
        elif operation == "-":
            result = first_number_or_string - second_number_or_string
            print(result)
        elif operation == "*":
            result = first_number_or_string * second_number_or_string
            print(result)
        elif operation == "/":
            result = first_number_or_string / second_number_or_string
            print(result)
        elif operation == "//":
            result = first_number_or_string // second_number_or_string
            print(result)
        elif operation == "%":
            result = first_number_or_string % second_number_or_string
            print(result)
        else:
            return False

    calculator(first_checked_value, second_checked_value, op_checked_value)

    out = int(input("Enter '1' to continue. Otherwise enter 0 to exit: "))
