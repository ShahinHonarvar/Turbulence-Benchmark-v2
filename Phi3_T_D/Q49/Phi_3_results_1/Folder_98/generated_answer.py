def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    fib_14 = fibonacci(14)
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_14 == 0