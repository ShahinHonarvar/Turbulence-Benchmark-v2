def if_decimal_is_divisible(binary_str):
    n = len(binary_str)
    decimal_num = int(binary_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    fib_num = fibonacci(54)
    return decimal_num % fib_num == 0