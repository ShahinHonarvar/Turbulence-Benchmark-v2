def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a

    def to_decimal(binary_str):
        return int(binary_str, 2)
    fib_19th = fibonacci(19)
    decimal_value = to_decimal(binary_string)
    return decimal_value % fib_19th == 0