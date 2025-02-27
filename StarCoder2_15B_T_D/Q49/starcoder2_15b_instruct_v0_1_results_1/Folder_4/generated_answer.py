def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, 2)
    fibonacci_118 = 7778742049
    return decimal_int % fibonacci_118 == 0