def if_decimal_is_divisible(bin_str):
    fib_seq = [0, 1]
    while len(fib_seq) < 85:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fib_84th = fib_seq[-1]
    dec_val = int(bin_str, 2)
    return dec_val % fib_84th == 0