def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fibo_value = fibonacci(67)
    return decimal_value % fibo_value == 0