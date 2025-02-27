def if_decimal_is_divisible(binary_str):
    decimal_val = int(binary_str, 2)
    fibonacci_15 = 377
    return decimal_val % fibonacci_15 == 0