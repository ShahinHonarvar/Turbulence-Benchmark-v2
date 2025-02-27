def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, base=2)
    fibonacci_107 = 147625497578125
    return decimal_integer % fibonacci_107 == 0