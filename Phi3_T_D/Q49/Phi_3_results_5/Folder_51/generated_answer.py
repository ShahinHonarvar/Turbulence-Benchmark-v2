def if_decimal_is_divisible(binary_str):

    def decimal(binary):
        return int(binary, 2)

    def fibonacci_17_th():
        a, b = (0, 1)
        for _ in range(17):
            a, b = (b, a + b)
        return a
    fib_17th = fibonacci_17_th()
    return decimal(binary_str) % fib_17th == 0