def convert_to_decimal(binary_str):
    return int(binary_str, 2)

def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def fibonacci_115():
    return fibonacci(115)

def if_decimal_is_divisible(binary_str):
    decimal_num = convert_to_decimal(binary_str)
    fib_115 = fibonacci_115()
    return decimal_num % fib_115 == 0