def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_74 = fibonacci(74)
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_74 == 0