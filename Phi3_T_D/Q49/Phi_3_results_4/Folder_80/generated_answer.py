from math import sqrt

def if_decimal_is_divisible(binary_str):

    def is_fibonacci(n):
        return sqrt(5 * n ** 2 + 4).is_integer() or sqrt(5 * n ** 2 - 4).is_integer()

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal = int(binary_str, 2)
    fib_seq = [0, 1]
    while len(fib_seq) < 179:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    if_val = fib_seq[-1]
    return decimal % if_val == 0