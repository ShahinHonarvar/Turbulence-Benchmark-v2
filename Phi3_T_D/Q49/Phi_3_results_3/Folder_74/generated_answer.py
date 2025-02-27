def if_decimal_is_divisible(binary_str):
    fibonacci_166 = fibonacci(166)
    decimal_int = int(binary_str, 2)
    return decimal_int % fibonacci_166 == 0

def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a