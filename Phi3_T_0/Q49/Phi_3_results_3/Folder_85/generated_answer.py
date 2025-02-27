def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib_45 = fibonacci(45)
    decimal_num = binary_to_decimal(binary_str)
    return decimal_num % fib_45 == 0