def if_decimal_is_divisible(binary_string):
    fib_seq = [0, 1, 1]
    while len(fib_seq) < 196:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    decimal_number = int(binary_string, 2)
    return decimal_number % fib_seq[-1] == 0