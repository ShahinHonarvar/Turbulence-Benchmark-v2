def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    for _ in range(15):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fibonacci_17th = fib_sequence[16]
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_17th == 0