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


if __name__ == '__main__':
     var_input_for_numbers("Enter numbers")