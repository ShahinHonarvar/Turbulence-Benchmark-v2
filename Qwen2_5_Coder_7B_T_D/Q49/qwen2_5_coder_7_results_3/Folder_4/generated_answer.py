def if_decimal_is_divisible(binary_str):
    fib_num = 117
    a, b = (0, 1)
    for _ in range(fib_num - 1):
        a, b = (b, a + b)
    return int(binary_str, 2) % b == 0