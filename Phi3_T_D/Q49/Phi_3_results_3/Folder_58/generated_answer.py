def if_decimal_is_divisible(binary):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    decimal = binary_to_decimal(binary)
    fib_105 = fibonacci(105)
    return decimal % fib_105 == 0