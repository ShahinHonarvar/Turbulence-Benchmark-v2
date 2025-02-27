def if_decimal_is_divisible(binary_str):
    fib_seq = [0, 1]
    while len(fib_seq) < 189:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    if int(binary_str, 2) % fib_seq[188] == 0:
        return True
    else:
        return False