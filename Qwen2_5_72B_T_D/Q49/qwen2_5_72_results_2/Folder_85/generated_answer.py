def if_decimal_is_divisible(binary_str):
    a, b = (0, 1)
    for _ in range(43):
        a, b = (b, a + b)
    fib_45 = b
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_45 == 0