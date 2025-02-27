def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    for _ in range(14):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fibonacci_15th = fib_sequence[14]
    decimal_number = int(binary_str, 2)
    return decimal_number % fibonacci_15th == 0