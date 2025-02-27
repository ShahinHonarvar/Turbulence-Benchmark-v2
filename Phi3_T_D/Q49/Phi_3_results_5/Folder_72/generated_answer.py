def if_decimal_is_divisible(binary_str):
    fib_seq = [0, 1]
    while len(fib_seq) < 175:
        next_fib = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_fib)
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_seq[174] == 0