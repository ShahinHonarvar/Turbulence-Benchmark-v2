def if_decimal_is_divisible(binary_str):
    fib_56 = 0
    a, b = (0, 1)
    while len(str(a)) < len(binary_str):
        a, b = (b, a + b)
    fib_56 = a
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_56 == 0