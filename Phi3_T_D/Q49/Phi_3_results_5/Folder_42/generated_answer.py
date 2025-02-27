def if_decimal_is_divisible(binary_str):

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)

    def fibonacci_146th():
        a, b = (0, 1)
        for _ in range(146):
            a, b = (b, a + b)
        return a
    fib146 = fibonacci_146th()
    decimal_value = binary_to_decimal(binary_str)
    return decimal_value % fib146 == 0