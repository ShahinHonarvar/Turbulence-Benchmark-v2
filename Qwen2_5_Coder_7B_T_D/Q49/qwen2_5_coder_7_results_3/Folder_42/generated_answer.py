def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(bin_str):
        return int(bin_str, 2)
    fib_146 = fibonacci(146)
    decimal_num = binary_to_decimal(binary_str)
    return decimal_num % fib_146 == 0