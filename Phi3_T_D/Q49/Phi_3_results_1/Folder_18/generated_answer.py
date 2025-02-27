def if_decimal_is_divisible(binary_str):
    fib_199 = calculate_fibonacci_number(199)
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_199 == 0

def calculate_fibonacci_number(n):
    if n in {0, 1}:
        return n
    a, b = (0, 1)
    for _ in range(n - 1):
        a, b = (b, a + b)
    return b