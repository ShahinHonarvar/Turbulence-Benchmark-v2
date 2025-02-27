def if_decimal_is_divisible(binary_str):
    fib_numbers = [0, 1]
    for _ in range(2, 125):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_numbers[124] == 0