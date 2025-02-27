def if_decimal_is_divisible(binary_representation_string: str) -> bool:
    decimal_integer = int(binary_representation_string, 2)
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    fibonacci_number = (phi ** decimal_integer - psi ** decimal_integer) / 5 ** 0.5
    if fibonacci_number % 64 == 0:
        return True
    else:
        return False