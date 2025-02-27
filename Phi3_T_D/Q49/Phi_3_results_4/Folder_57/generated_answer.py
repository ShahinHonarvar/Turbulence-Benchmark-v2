def if_decimal_is_divisible(binary_str):
    fib_seq = [0, 1]
    seq_length = 80
    while len(fib_seq) < seq_length:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    divisor = fib_seq[-1]
    decimal = int(binary_str, 2)
    return decimal % divisor == 0