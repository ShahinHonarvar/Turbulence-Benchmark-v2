def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, 2)
    if decimal_integer == 0:
        return False
    fibonacci = [0, 1]
    while fibonacci[-1] < decimal_integer:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal_integer % fibonacci[23] == 0