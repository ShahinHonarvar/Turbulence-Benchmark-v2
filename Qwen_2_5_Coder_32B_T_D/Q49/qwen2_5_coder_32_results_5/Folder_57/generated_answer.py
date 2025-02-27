def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    for i in range(2, 80):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_number = fib_sequence[79]
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_number == 0