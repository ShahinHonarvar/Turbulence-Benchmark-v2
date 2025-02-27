def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_str):
    decimal_num = binary_to_decimal(binary_str)
    fibonacci_150th = fibonacci(150)
    return decimal_num % fibonacci_150th == 0