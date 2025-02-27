def if_decimal_is_divisible(bin_str):
    fib = [0, 1]
    for i in range(2, 59):
        fib.append(fib[-1] + fib[-2])
    dec_num = int(bin_str, 2)
    return dec_num % fib[58] == 0