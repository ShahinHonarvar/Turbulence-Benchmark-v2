def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, 2)
    fibonacci_numbers = [0, 1]
    current_number = 0
    while current_number < decimal_int:
        current_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(current_number)
    return decimal_int in fibonacci_numbers[177:]