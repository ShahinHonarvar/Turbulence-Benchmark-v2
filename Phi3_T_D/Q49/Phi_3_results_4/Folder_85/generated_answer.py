def if_decimal_is_divisible(binary_str):
    fib_indices = [0, 1]
    while fib_indices[-1] < 45:
        fib_indices.append(fib_indices[-1] + fib_indices[-2])
    target_fib_number = fib_indices[-1]
    decimal_number = int(binary_str, 2)
    return decimal_number % target_fib_number == 0