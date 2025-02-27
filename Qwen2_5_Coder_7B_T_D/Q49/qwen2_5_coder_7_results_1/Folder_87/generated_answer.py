def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(binary):
        return int(binary, 2)
    fib_180 = fibonacci(180)
    decimal = binary_to_decimal(binary_str)
    return decimal % fib_180 == 0