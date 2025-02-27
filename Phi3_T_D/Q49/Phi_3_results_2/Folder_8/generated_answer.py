def if_decimal_is_divisible(binary_str):

    def fibonacci_54th():
        a, b = (0, 1)
        for _ in range(53):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib_54th = fibonacci_54th()
    decimal_value = binary_to_decimal(binary_str)
    return decimal_value % fib_54th == 0