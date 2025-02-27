def if_decimal_is_divisible(binary_str):

    def fibonacci_sequence(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    fib_34 = fibonacci_sequence(35)
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_34 == 0