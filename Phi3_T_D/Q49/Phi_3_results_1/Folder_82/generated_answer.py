def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_rep):
    decimal_value = binary_to_decimal(binary_rep)
    fibonacci_99th = fibonacci(99)
    return decimal_value % fibonacci_99th == 0