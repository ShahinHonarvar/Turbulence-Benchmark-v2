def if_decimal_is_divisible(binary_str):
    fibonacci_16th = 144
    decimal_number = int(binary_str, 2)
    return decimal_number % fibonacci_16th == 0