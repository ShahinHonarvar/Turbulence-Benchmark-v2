def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_sequence[6] == 0