def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    is_divisible = decimal_integer % 678961119047220872775898887318292449863798631511811556745031427457031186488153141 == 0
    return is_divisible