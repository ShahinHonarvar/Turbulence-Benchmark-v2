def if_decimal_is_divisible(binary_str: str) -> bool:
    decimal_int = int(binary_str, 2)
    first_99_fibonacci_number = 218922995834555169026
    return decimal_int % first_99_fibonacci_number == 0