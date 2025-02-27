def if_decimal_is_divisible(binary_str):

    def fibonacci_sequence(n):
        sequence = [0, 1]
        while len(sequence) <= n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence
    fib_107th = fibonacci_sequence(107)[-1]
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_107th == 0