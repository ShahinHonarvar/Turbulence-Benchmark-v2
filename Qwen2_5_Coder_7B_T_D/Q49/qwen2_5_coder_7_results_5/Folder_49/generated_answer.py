def if_decimal_is_divisible(binary_str):
    fib_number = 95
    a, b = (0, 1)
    for _ in range(fib_number):
        a, b = (b, a + b)
    decimal_number = int(binary_str, 2)
    return decimal_number % a == 0