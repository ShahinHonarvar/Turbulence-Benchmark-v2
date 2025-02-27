def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_186 = fibonacci(186)
    decimal = int(binary_str, 2)
    return decimal % fib_186 == 0