def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_90 = fibonacci(90)
    decimal = int(binary_str, 2)
    return decimal % fib_90 == 0