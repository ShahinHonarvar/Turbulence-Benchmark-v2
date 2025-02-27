def if_decimal_is_divisible(bin_str):
    a, b = (0, 1)
    for _ in range(66):
        a, b = (b, a + b)
    fib_67 = b
    dec_num = int(bin_str, 2)
    return dec_num % fib_67 == 0