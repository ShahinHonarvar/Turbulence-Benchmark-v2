def if_decimal_is_divisible(binary_str):
    fib_54 = 832040
    decimal_val = int(binary_str, 2)
    return decimal_val % fib_54 == 0