def if_decimal_is_divisible(binary_string):
    decimal_val = int(binary_string, 2)
    fib_20 = 6765
    return decimal_val % fib_20 == 0