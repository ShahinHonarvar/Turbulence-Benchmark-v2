def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21]
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_sequence[8] == 0