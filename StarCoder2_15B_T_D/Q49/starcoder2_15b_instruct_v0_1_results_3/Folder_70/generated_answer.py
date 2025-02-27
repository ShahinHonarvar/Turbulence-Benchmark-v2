def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_137 = 1 / sqrt(5) * ((1 + sqrt(5)) ** 137 - (1 - sqrt(5)) ** 137)
    return decimal_integer % fibonacci_137 == 0