def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    a, b = (0, 1)
    fibonacci_sequence = [a, b]
    while True:
        a, b = (b, a + b)
        fibonacci_sequence.append(b)
        if len(fibonacci_sequence) == 87:
            break
    return decimal_integer % fibonacci_sequence[-1] == 0