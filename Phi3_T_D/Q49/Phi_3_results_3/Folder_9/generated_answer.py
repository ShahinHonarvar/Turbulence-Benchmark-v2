def if_decimal_is_divisible(binary_str):
    n = 2
    a, b = (0, 1)
    fib_68 = 0
    while n <= 68:
        fib_68 = a
        a, b = (b, a + b)
        n += 1
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_68 == 0