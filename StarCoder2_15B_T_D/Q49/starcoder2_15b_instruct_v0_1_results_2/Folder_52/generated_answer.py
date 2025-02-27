def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    if decimal_integer == 0:
        return False
    a, b = (0, 1)
    counter = 1
    while a <= decimal_integer:
        if a == decimal_integer:
            return counter % 176 == 0
        a, b = (b, a + b)
        counter += 1
    return False