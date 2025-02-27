def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    for i in range(2, 46):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_46 = fib_sequence[45]
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_46 == 0