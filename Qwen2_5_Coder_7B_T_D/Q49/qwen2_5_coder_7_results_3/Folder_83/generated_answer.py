def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n <= 1:
            return n
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib_60 = fibonacci(60)
    decimal = binary_to_decimal(binary_str)
    return decimal % fib_60 == 0