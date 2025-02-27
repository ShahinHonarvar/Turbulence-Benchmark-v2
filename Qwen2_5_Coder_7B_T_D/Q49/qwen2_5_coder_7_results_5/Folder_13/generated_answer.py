def if_decimal_is_divisible(binary_str):
    fibonacci_numbers = [0, 1]
    for i in range(2, 175):
        next_fib = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_fib)
    divisor = fibonacci_numbers[174]
    decimal_number = int(binary_str, 2)
    return decimal_number % divisor == 0