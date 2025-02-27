def if_decimal_is_divisible(binary_str):
    fib_seq = [0, 1]
    fib_127 = 0
    while len(fib_seq) <= 127:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fib_127 = fib_seq[127]
    decimal = int(binary_str, 2)
    return decimal % fib_127 == 0