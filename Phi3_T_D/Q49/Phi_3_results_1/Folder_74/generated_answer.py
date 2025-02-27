def is_decimal_divisible(binary_str):

    def fib_number(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib = fib_number(166)
    decimal_num = binary_to_decimal(binary_str)
    return decimal_num % fib == 0