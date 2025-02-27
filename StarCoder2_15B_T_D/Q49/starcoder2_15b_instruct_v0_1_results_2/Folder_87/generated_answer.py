def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, base=2)

    def calculate_180th_fibonacci_number() -> int:
        a, b = (0, 1)
        for _ in range(179):
            a, b = (b, a + b)
        return b
    return decimal_integer % calculate_180th_fibonacci_number() == 0