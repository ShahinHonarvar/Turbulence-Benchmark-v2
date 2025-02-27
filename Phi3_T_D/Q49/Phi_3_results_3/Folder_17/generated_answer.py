def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, 2)
    fib_154 = fibonacci(154)
    return decimal_int % fib_154 == 0