def if_decimal_is_divisible(binary_str):
    fib_numbers = [0, 1]
    for _ in range(8):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    ten_fib_number = fib_numbers[9]
    decimal_number = int(binary_str, 2)
    return decimal_number % ten_fib_number == 0