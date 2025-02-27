def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_196 = (1 + 5 ** 0.5) ** 196 / (2 ** 196 * 5 ** 0.5) + 0.5
    return decimal_integer % fibonacci_196 == 0