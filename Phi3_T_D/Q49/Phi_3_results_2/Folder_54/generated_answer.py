def if_decimal_is_divisible(binary_str):

    def fibonacci():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)

    def is_divisible_by_fibonacci_34(decimal):
        fib_gen = fibonacci()
        for _ in range(34):
            next(fib_gen)
        return decimal % next(fib_gen) == 0
    decimal = binary_to_decimal(binary_str)
    return is_divisible_by_fibonacci_34(decimal)