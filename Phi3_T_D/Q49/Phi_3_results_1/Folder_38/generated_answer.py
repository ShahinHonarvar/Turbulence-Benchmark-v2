def if_decimal_is_divisible(binary_string):
    fib_80 = 267914296
    decimal_value = int(binary_string, 2)
    return decimal_value % fib_80 == 0