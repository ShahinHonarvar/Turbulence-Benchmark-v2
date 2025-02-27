def if_decimal_is_divisible(binary_str):
    fib_16 = 987
    decimal_val = int(binary_str, 2)
    return decimal_val % fib_16 == 0