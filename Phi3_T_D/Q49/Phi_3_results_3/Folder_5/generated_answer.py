def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib_n_1, fib_n_2 = (0, 1)
    while fib_n_2 < decimal_num:
        next_fib = fib_n_1 + fib_n_2
        fib_n_1, fib_n_2 = (fib_n_2, next_fib)
        n = 71
        while fib_n_2 < decimal_num:
            fib_n_1, fib_n_2 = (fib_n_2, fib_n_1 + fib_n_2)
            n -= 1
    return decimal_num % fib_n_1 == 0