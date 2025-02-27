def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, 2)
    fibonacci_numbers = [0, 1]
    for i in range(2, 20):
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)
    return decimal_int % fibonacci_numbers[18] == 0