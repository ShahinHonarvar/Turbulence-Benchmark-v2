def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    if decimal_integer < 0:
        raise ValueError('The given string is not a binary representation of a non-negative decimal integer.')
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < decimal_integer:
        fibonacci_sequence.append(fibonacci_sequence[-2] + fibonacci_sequence[-1])
    if decimal_integer in fibonacci_sequence:
        return decimal_integer == fibonacci_sequence[195]
    else:
        return False