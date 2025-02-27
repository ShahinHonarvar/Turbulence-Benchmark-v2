def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib_134 = fibonacci(134)
    decimal_number = binary_to_decimal(binary_str)
    return decimal_number % fib_134 == 0