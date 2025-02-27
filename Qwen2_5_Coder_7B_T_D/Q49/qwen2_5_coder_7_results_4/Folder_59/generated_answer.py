def if_decimal_is_divisible(binary_str):
    fib_74 = 1
    a, b = (0, 1)
    for _ in range(73):
        a, b = (b, a + b)
    dec_num = int(binary_str, 2)
    return dec_num % fib_74 == 0