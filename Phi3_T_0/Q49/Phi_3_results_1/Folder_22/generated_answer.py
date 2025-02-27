def if_decimal_is_divisible(binary_str):
    fib_20 = 6765
    decimal_val = int(binary_str, 2)
    return decimal_val % fib_20 == 0