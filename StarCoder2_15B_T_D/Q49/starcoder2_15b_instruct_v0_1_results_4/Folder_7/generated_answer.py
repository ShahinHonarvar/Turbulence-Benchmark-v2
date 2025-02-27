def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, base=2)
    phi = (1 + 5 ** 0.5) / 2
    fibonacci_160 = (phi ** 160 - (1 - phi) ** 160) / 5 ** 0.5
    if decimal_integer % fibonacci_160 == 0:
        return True
    else:
        return False