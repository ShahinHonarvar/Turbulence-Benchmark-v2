def if_decimal_is_divisible(bin_str):
    a, b = (0, 1)
    fib_150 = 0
    for _ in range(150):
        a, b = (b, a + b)
        fib_150 = b
    dec_num = int(bin_str, 2)
    return dec_num % fib_150 == 0