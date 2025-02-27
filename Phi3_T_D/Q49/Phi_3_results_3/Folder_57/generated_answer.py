def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fibonacci_80th = fibonacci(80)
    return decimal % fibonacci_80th == 0