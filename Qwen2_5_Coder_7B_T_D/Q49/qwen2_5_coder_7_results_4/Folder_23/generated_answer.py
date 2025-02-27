def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib_48 = fibonacci(48)
    decimal_value = binary_to_decimal(binary_str)
    return decimal_value % fib_48 == 0