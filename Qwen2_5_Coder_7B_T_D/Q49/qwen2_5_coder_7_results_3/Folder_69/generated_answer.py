def if_decimal_is_divisible(bin_str):
    fib = [0, 1]
    for i in range(2, 171):
        fib.append(fib[-1] + fib[-2])
    fib_170 = fib[170]
    dec_num = int(bin_str, 2)
    return dec_num % fib_170 == 0