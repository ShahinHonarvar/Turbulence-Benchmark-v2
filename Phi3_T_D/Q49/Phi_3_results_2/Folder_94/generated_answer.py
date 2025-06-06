def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_40 = fibonacci(40)
    return decimal % fib_40 == 0