def if_decimal_is_divisible(binary_str):
    a, b = (0, 1)
    for _ in range(95 - 1):
        a, b = (b, a + b)
    fibonacci_95 = b
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_95 == 0