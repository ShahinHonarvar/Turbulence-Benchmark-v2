def if_decimal_is_divisible(binary_representation_str):
    decimal_number = int(binary_representation_str, 2)
    return decimal_number % 17711 == 0