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

if __name__ == '__main__':
    cul = calculator_main()