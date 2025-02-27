def if_decimal_is_divisible(binary_str):
    fib_29 = 0
    a, b = (0, 1)
    for _ in range(29):
        a, b = (b, a + b)
    fib_29 = b
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_29 == 0