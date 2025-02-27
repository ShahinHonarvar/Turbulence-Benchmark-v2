def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, 2)
    fibonacci_116 = 832040
    fibonacci_115 = 531441
    fibonacci_117 = fibonacci_116 + fibonacci_115
    return decimal_integer % fibonacci_117 == 0