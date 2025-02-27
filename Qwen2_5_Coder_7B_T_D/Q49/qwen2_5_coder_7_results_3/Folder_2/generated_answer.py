def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_125 = fibonacci(125)
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_125 == 0