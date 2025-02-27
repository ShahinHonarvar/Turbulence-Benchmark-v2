def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, 2)
    fibonacci_num = fibonacci_sequence[94]
    return decimal_int % fibonacci_num == 0

def generate_fibonacci_sequence():
    a, b = (0, 1)
    fibonacci_sequence = []
    while len(fibonacci_sequence) < 95:
        fibonacci_sequence.append(a)
        a, b = (b, a + b)
    return fibonacci_sequence