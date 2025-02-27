def if_decimal_is_divisible(binary_str):

    def get_fibonacci_n(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal = int(binary_str, 2)
    fib_97 = get_fibonacci_n(97)
    return decimal % fib_97 == 0