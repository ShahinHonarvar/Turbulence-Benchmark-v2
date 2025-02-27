def if_decimal_is_divisible(binary_str):

    def fibonacci_sequence():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib_sequence = fibonacci_sequence()
    fib_186 = next((next(fib_sequence) for _ in range(186)))
    decimal_number = binary_to_decimal(binary_str)
    return decimal_number % fib_186 == 0