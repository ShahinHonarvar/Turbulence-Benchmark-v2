def if_decimal_is_divisible(binary_str):
    fibonacci_49 = 1512709447
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_49 == 0