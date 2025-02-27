def if_decimal_is_divisible(binary_repr: str) -> bool:
    decimal_repr = 0
    for i, bit in enumerate(reversed(binary_repr)):
        if bit == '1':
            decimal_repr += 2 ** i
    if decimal_repr % fibonacci(186) == 0:
        return True
    else:
        return False

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)