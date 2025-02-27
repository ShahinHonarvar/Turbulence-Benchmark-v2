def if_decimal_is_divisible(binary_string):

    def fib_sequence(n):
        a, b = (0, 1)
        sequence = [a]
        while len(sequence) <= n:
            a, b = (b, a + b)
            sequence.append(a)
        return sequence[n]
    decimal = int(binary_string, 2)
    fib_28 = fib_sequence(27)
    return decimal % fib_28 == 0