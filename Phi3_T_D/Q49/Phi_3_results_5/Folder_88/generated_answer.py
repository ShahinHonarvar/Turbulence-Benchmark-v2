def if_decimal_is_divisible(binary_str):
    fib_seq = [0, 1]
    fib_49th = 0
    while len(fib_seq) < 50:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fib_49th = fib_seq[-1]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_49th == 0