def if_decimal_is_divisible(binary_str):
    fib_150 = 0
    a, b = (0, 1)
    for _ in range(150):
        a, b = (b, a + b)
        fib_150 = b
    decimal = int(binary_str, 2)
    return decimal % fib_150 == 0