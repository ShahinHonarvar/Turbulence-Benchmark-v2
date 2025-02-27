def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_numbers = [0, 1]
    while fibonacci_numbers[-1] < decimal_integer:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return decimal_integer in fibonacci_numbers[120:]