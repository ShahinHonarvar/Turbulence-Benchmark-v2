def if_decimal_is_divisible(binary_str):
    fibonacci_17 = 1597
    decimal_int = int(binary_str, 2)
    return decimal_int % fibonacci_17 == 0