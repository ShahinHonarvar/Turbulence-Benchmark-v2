def if_decimal_is_divisible(binary_str):
    fib_40 = 102334155
    decimal_val = int(binary_str, 2)
    return decimal_val % fib_40 == 0