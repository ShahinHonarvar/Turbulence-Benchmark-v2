def if_decimal_is_divisible(binary_str):
    fib_seq = [0, 1]
    for i in range(2, 135):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fib_134 = fib_seq[134]
    decimal = int(binary_str, 2)
    return decimal % fib_134 == 0