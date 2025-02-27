def if_decimal_is_divisible(binary_str):
    a, b = (0, 1)
    for i in range(175):
        a, b = (b, a + b)
    fib_175 = a
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_175 == 0