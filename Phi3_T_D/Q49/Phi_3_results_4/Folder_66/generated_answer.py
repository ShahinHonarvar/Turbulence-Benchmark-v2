def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for i in range(n):
            a, b = (b, a + b)
        return a
    decimal = int(binary_string, 2)
    fib_120th = fibonacci(120)
    return decimal % fib_120th == 0