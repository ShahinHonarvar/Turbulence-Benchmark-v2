def if_decimal_is_divisible(binary_str):
    fib_seq = [0, 1]
    while len(fib_seq) <= 109:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_seq[108] == 0