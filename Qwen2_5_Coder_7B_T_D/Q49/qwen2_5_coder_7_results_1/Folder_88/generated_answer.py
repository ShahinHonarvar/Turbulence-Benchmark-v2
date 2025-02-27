def if_decimal_is_divisible(binary_str):
    fib_seq = [0, 1]
    for i in range(2, 49):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fib_49 = fib_seq[48]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_49 == 0