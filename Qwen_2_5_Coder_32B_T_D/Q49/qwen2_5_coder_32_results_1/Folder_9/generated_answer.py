def if_decimal_is_divisible(binary_str):
    a, b = (0, 1)
    for _ in range(67):
        a, b = (b, a + b)
    fib_68 = a
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_68 == 0