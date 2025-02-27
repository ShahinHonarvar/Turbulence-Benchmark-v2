def if_decimal_is_divisible(binary_str: str) -> bool:
    decimal_int = int(binary_str, base=2)
    fibonacci_20 = 6765
    return decimal_int % fibonacci_20 == 0