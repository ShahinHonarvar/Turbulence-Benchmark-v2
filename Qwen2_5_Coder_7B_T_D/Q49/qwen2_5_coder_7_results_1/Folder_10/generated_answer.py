def if_decimal_is_divisible(binary_str):
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < 88:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    nth_fibonacci = fibonacci_numbers[87]
    decimal_number = int(binary_str, 2)
    return decimal_number % nth_fibonacci == 0