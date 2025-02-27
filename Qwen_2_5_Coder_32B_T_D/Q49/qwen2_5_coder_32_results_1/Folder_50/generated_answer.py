def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    for i in range(2, 119):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    divisor = fib_sequence[118]
    decimal_number = int(binary_str, 2)
    return decimal_number % divisor == 0