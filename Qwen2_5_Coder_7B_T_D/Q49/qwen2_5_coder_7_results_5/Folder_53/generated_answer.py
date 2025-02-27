def if_decimal_is_divisible(binary_str):
    fib_64 = 144
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_64 == 0