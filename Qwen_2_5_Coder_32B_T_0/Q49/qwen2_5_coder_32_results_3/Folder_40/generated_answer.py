def if_decimal_is_divisible(binary_str):
    fib_4th = 3
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_4th == 0