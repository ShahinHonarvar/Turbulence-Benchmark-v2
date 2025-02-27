def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    target_fib_number = fib(69)
    decimal_number = binary_to_decimal(binary_str)
    return decimal_number % target_fib_number == 0