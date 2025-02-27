def if_decimal_is_divisible(binary_str):
    fib, a, b = (0, 0, 1)
    while fib < 88:
        a, b = (b, a + b)
        fib += 1
    decimal_number = int(binary_str, 2)
    return decimal_number % a == 0