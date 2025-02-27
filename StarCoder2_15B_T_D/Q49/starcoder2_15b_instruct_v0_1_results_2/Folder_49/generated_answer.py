def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    first, second = (0, 1)
    for _ in range(94):
        first, second = (second, first + second)
    if decimal_integer % second == 0:
        return True
    else:
        return False