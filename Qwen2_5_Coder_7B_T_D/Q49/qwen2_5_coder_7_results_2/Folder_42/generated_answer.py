def if_decimal_is_divisible(binary_str):
    fib_seq = [0, 1]
    for i in range(2, 147):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fib_146 = fib_seq[146]
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_146 == 0