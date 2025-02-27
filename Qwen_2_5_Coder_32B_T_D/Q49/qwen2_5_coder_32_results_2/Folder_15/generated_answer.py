def if_decimal_is_divisible(binary_string):
    fib_sequence = [0, 1]
    for i in range(2, 9):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_nine = fib_sequence[8]
    decimal_value = int(binary_string, 2)
    return decimal_value % fib_nine == 0