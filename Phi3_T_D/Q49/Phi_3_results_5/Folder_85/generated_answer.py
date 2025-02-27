def if_decimal_is_divisible(binary_str):
    fibonacci_45 = 1134903170
    decimal_num = int(binary_str, 2)
    return decimal_num % fibonacci_45 == 0