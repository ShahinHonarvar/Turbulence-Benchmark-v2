def if_decimal_is_divisible(binary_str):
    fib_40 = 0
    a, b = (0, 1)
    for _ in range(40):
        fib_40 = a
        a, b = (b, a + b)
    dec_num = int(binary_str, 2)
    return dec_num % fib_40 == 0