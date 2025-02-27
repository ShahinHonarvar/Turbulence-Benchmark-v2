def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    decimal_number = int(binary_str, 2)
    fib_40 = fibonacci(40)
    return decimal_number % fib_40 == 0