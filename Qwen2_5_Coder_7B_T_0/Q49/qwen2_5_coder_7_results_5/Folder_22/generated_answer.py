def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_20 = fibonacci(20)
    decimal = int(binary_str, 2)
    return decimal % fib_20 == 0