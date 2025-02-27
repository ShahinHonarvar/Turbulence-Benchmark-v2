def if_decimal_is_divisible(binary_str):
    a, b = (0, 1)
    for _ in range(78):
        a, b = (b, a + b)
    fib_78 = a
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_78 == 0