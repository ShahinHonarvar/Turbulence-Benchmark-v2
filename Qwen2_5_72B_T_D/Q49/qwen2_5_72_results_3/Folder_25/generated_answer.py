def if_decimal_is_divisible(binary_str):
    fib_seq = [0, 1]
    for i in range(2, 19):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fib_19 = fib_seq[18]
    decimal_val = int(binary_str, 2)
    return decimal_val % fib_19 == 0