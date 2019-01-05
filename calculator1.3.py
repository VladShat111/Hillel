from method_for_calculator.check_input_for_numbers import var_input_for_numbers
from method_for_calculator.check_input_for_operation_symbol import var_input_for_op
from method_for_calculator.check_for_division_operations import division_check
from method_for_calculator.main_operation_for_calculator import calculator_main


result = 0
out = None

while out != 0:


    first_checked_value = var_input_for_numbers("Enter first number: ")
    second_checked_value = var_input_for_numbers("Enter second number: ")
    op_checked_value = var_input_for_op("operation: ")



    division_check(first_checked_value, second_checked_value, op_checked_value)
    calculator_main(first_checked_value, second_checked_value, op_checked_value)

    out = int(input("Enter '1' to continue. Otherwise enter 0 to exit: "))
