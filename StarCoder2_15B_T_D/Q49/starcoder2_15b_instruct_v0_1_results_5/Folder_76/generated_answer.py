def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, base=2)
    first_188_fibonacci_number = 176006511938862812038186486472216240755586583855830393468651688391270360887627126726162874369172938314254987599
    return decimal_integer % first_188_fibonacci_number == 0