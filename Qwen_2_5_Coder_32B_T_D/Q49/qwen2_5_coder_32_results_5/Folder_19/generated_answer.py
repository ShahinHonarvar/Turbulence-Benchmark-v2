def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    while len(fib_sequence) <= 29:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    divisible_number = fib_sequence[29]
    decimal_number = int(binary_str, 2)
    return decimal_number % divisible_number == 0