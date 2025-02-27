def if_decimal_is_divisible(bin_str):
    fib_138 = 0
    fib_139 = 1
    num = int(bin_str, 2)
    while fib_138 < num:
        fib_tmp = fib_138 + fib_139
        fib_138, fib_139 = (fib_139, fib_tmp)
    return num % fib_138 == 0