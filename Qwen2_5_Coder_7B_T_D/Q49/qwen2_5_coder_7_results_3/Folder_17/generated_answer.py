def if_decimal_is_divisible(binary_str):
    a, b = (0, 1)
    fib_154 = None
    for _ in range(154):
        a, b = (b, a + b)
    fib_154 = b
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_154 == 0