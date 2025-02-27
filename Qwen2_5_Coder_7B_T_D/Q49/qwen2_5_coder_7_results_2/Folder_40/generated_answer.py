def if_decimal_is_divisible(binary_str):
    fib_seq = [0, 1, 1]
    while len(fib_seq) < 4:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fourth_fib = fib_seq[3]
    decimal_num = int(binary_str, 2)
    return decimal_num % fourth_fib == 0