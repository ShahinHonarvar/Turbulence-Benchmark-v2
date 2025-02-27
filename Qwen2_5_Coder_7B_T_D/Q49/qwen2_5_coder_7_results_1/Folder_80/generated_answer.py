def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib_179 = fib(179)
    decimal_number = binary_to_decimal(binary_str)
    return decimal_number % fib_179 == 0