def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    for _ in range(57):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_59th = fib_sequence[58]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_59th == 0