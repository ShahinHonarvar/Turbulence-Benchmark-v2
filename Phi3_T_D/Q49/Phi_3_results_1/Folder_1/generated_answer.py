def fib_to_n(n):
    a, b = (0, 1)
    fib_sequence = []
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = (b, a + b)
    return fib_sequence[-1]

def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fib_90th = fib_to_n(90)
    return decimal_number % fib_90th == 0