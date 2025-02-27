def if_decimal_is_divisible(binary_str):
    fib_seq = [0, 1]
    decimal = int(binary_str, 2)
    while len(fib_seq) < 87:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return decimal % fib_seq[86] == 0