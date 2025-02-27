def if_decimal_is_divisible(binary_str):
    fib_10 = 34
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_10 == 0