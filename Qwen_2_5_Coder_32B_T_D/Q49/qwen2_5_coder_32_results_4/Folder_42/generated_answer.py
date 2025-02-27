def if_decimal_is_divisible(binary_str):

    def fibonacci_generator(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_146 = fibonacci_generator(145)
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_146 == 0