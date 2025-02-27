def if_decimal_is_divisible(binary_str):

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)

    def fibonacci_at_n(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal = binary_to_decimal(binary_str)
    fib_59 = fibonacci_at_n(59)
    return decimal % fib_59 == 0