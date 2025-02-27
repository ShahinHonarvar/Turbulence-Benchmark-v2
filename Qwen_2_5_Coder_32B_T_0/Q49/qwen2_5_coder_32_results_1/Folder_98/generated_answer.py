def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    for i in range(2, 14):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_14th = fib_sequence[13]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_14th == 0