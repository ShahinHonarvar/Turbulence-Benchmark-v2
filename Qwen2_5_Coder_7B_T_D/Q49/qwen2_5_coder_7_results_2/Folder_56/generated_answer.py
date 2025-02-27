def if_decimal_is_divisible(binary_str):
    fibonacci_number = 0
    a, b = (0, 1)
    for _ in range(83):
        a, b = (b, a + b)
    divisor = b
    decimal_number = int(binary_str, 2)
    return decimal_number % divisor == 0