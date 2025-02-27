def if_decimal_is_divisible(binary_string):
    fib_15 = 377
    decimal_number = int(binary_string, 2)
    return decimal_number % fib_15 == 0