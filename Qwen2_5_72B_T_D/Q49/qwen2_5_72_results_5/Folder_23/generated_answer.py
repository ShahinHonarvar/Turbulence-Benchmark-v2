def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_48 = fibonacci(47)
    decimal = int(binary_str, 2)
    return decimal % fib_48 == 0