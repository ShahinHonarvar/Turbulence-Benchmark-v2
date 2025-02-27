def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    for i in range(2, 48):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_48th = fib_sequence[47]
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_48th == 0