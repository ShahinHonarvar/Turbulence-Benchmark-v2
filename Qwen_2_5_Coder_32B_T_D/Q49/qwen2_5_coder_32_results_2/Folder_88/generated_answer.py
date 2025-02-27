def if_decimal_is_divisible(binary_str):
    a, b = (0, 1)
    for _ in range(49):
        a, b = (b, a + b)
    fib_49 = a
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_49 == 0