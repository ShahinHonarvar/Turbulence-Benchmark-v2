def if_decimal_is_divisible(binary_str):
    fibo_175 = fibonacci(175)
    decimal = int(binary_str, 2)
    return decimal % fibo_175 == 0

def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a