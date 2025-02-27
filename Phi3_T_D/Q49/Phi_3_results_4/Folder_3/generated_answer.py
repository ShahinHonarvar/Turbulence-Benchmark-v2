def if_decimal_is_divisible(binary_str):
    fib_35 = 14930352
    decimal_val = int(binary_str, 2)
    return decimal_val % fib_35 == 0