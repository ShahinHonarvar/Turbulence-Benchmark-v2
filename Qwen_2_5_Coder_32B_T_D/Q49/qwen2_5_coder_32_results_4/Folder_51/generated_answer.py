def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    for i in range(2, 17):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_17 = fib_sequence[16]
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_17 == 0