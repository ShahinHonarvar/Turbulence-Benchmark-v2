def if_decimal_is_divisible(binary_str):
    fibonacci_sixth = 8
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_sixth == 0