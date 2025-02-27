def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_7th = 0
    a, b = (0, 1)
    for _ in range(6):
        a, b = (b, a + b)
    fibonacci_7th = b
    return decimal % fibonacci_7th == 0