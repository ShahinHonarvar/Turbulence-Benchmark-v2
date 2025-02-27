def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    current_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    while current_number < decimal_integer:
        fibonacci_sequence.append(current_number)
        current_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    return decimal_integer in fibonacci_sequence