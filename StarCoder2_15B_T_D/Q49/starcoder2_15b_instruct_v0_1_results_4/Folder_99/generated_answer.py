def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_109th = 6798916376386122581618101
    return decimal_integer % fibonacci_109th == 0