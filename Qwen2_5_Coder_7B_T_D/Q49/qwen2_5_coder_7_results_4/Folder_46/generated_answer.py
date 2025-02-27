def if_decimal_is_divisible(binary_str):
    fib_seq = [0, 1]
    for i in range(2, 139):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_seq[138] == 0