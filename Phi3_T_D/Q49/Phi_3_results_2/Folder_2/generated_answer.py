def if_decimal_is_divisible(binary_str):
    fibonacci_125 = round(((1 + 5 ** 0.5) / 2) ** 124)
    decimal_num = int(binary_str, 2)
    return decimal_num % fibonacci_125 == 0