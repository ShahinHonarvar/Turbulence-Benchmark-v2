def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    for _ in range(2, 27):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_27th = fib_sequence[26]
    return int(binary_str, 2) % fib_27th == 0