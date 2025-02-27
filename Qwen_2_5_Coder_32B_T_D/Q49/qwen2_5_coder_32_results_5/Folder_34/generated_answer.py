def if_decimal_is_divisible(binary_str):
    a, b = (0, 1)
    for _ in range(23):
        a, b = (b, a + b)
    fib_24 = b
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_24 == 0