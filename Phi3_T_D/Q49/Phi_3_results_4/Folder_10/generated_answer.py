def fib_sequence(n):
    a, b = (0, 1)
    sequence = []
    while len(sequence) < n:
        sequence.append(a)
        a, b = (b, a + b)
    return sequence[n - 1]

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def if_decimal_is_divisible(binary_str):
    decimal_int = binary_to_decimal(binary_str)
    fib_88th = fib_sequence(88)
    return decimal_int % fib_88th == 0