def if_decimal_is_divisible(binary_str):
    a, b = (0, 1)
    fib_195 = 0
    for _ in range(195):
        a, b = (b, a + b)
    fib_195 = b
    decimal = int(binary_str, 2)
    return decimal % fib_195 == 0