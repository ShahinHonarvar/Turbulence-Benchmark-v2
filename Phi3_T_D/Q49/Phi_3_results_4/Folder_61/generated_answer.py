def if_decimal_is_divisible(binary_string):
    dec_num = int(binary_string, 2)
    fib_seq = [0, 1]
    while len(fib_seq) < 76:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return dec_num % fib_seq[-1] == 0