def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    decimal_value = int(binary_str, 2)
    fib_number = fib(87)
    return decimal_value % fib_number == 0