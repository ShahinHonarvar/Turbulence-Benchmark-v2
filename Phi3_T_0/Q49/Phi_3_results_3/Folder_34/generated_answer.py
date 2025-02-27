def if_decimal_is_divisible(binary_str):
    fib_24 = 46368
    decimal_val = int(binary_str, 2)
    return decimal_val % fib_24 == 0