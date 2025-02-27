def fibonacci(n):
    a, b = (0, 1)
    for _ in range(2, n + 1):
        a, b = (b, a + b)
    return b

def if_decimal_is_divisible(binary_str):
    fib_13th = fibonacci(13)
    decimal = int(binary_str, 2)
    return decimal % fib_13th == 0