import math

def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    phi = (1 + math.sqrt(5)) / 2
    fibonacci_number = (phi ** 108 - (1 - phi) ** 108) / math.sqrt(5)
    return decimal_integer % fibonacci_number == 0