def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    for _ in range(2, 104):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_sequence[103] == 0