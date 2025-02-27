def if_decimal_is_divisible(binary_str):
    a, b = (0, 1)
    n = 0
    while n < 13:
        a, b = (b, a + b)
        n += 1
    fib_14 = b
    decimal = int(binary_str, 2)
    return decimal % fib_14 == 0