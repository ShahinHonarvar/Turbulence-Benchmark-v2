def if_decimal_is_divisible(binary_str):

    def fib(n):
        if n <= 1:
            return n
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    decimal_number = int(binary_str, 2)
    fib_186 = fib(186)
    return decimal_number % fib_186 == 0