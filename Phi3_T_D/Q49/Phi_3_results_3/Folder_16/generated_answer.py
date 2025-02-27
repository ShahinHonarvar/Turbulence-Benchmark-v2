def if_decimal_is_divisible(binary_str):
    fib_128th = 0
    a, b = (0, 1)
    for _ in range(128):
        a, b = (b, a + b)
    fib_128th = a
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_128th == 0