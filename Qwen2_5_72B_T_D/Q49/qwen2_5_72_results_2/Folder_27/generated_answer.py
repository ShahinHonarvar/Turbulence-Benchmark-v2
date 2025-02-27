def if_decimal_is_divisible(binary_str):
    a, b = (0, 1)
    for _ in range(85):
        a, b = (b, a + b)
    fib_87 = b
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_87 == 0