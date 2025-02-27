def if_decimal_is_divisible(binary_str):
    fib_sequence = get_fibonacci_sequence(118)
    decimal_number = int(binary_str, 2)
    if decimal_number % fib_sequence[-1] == 0:
        return True
    return False

def get_fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence