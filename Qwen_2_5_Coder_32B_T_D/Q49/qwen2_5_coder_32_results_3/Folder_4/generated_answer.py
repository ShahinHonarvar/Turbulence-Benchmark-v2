def if_decimal_is_divisible(binary_str):
    a, b = (0, 1)
    for _ in range(117):
        a, b = (b, a + b)
    fib_118 = b
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_118 == 0