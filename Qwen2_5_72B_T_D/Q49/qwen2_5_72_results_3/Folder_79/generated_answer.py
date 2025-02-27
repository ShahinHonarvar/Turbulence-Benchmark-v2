def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fib_sequence = [0, 1]
    for i in range(2, 13):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    divisor = fib_sequence[12]
    return decimal_value % divisor == 0