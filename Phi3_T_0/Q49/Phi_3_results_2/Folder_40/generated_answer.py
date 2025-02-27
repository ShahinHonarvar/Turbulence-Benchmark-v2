def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1, 1, 2]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_sequence[3] == 0