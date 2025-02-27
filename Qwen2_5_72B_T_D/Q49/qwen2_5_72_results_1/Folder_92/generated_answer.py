def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fib_sequence = [0, 1]
    for i in range(2, 7):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return decimal_value % fib_sequence[6] == 0