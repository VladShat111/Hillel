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

if __name__ == '__name__':
    div = division_check()