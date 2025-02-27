def if_decimal_is_divisible(binary_str):
    fib_20 = 6765
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_20 == 0