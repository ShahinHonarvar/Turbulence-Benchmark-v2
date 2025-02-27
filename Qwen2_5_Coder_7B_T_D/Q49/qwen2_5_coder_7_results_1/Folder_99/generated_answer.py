def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    dec = int(binary_str, 2)
    fib_109 = fibonacci(109)
    return dec % fib_109 == 0