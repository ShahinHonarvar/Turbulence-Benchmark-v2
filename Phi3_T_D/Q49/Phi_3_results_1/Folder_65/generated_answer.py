def if_decimal_is_divisible(bin_str):
    fib_seq = [0, 1]
    decimal = int(bin_str, 2)
    while len(fib_seq) < 127:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return decimal % fib_seq[126] == 0