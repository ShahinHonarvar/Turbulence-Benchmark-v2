def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) <= n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n]

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fibonacci_120 = fibonacci(120)
    decimal_value = binary_to_decimal(binary_str)
    return decimal_value % fibonacci_120 == 0