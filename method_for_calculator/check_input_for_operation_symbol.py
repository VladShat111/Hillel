def var_input_for_op(value):
    valid_operation = ['+', '-', '/', '*', '//', '%']
    if isinstance(value, str):
        while True:
            try:
                s = input("{}".format(value))
                if s in valid_operation:
                    return s
            except Exception as e:
                print("Error: use only valid operation: {} ".format(valid_operation), e)
    else:
        raise Exception("Please string")

if __name__ ==' __main__':
    op = var_input_for_op("Enter operation")