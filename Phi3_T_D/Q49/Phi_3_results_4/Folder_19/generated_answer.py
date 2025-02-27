def if_decimal_is_divisible(binary_string):
    fib_29 = 514229
    decimal_value = int(binary_string, 2)
    return decimal_value % fib_29 == 0