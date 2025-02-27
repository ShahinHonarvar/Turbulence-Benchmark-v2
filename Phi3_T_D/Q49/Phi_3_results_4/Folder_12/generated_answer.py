def if_decimal_is_divisible(binary_str):
    fib_seq = [0, 1]
    while True:
        next_fib = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_fib)
        if len(fib_seq) == 67:
            break
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_seq[66] == 0