def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    fibonacci_120 = (phi ** 120 - psi ** 120) / 5 ** 0.5
    if decimal_integer % fibonacci_120 == 0:
        return True
    else:
        return False