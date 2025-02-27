def if_decimal_is_divisible(binary_str):

    def fibonacci():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)
    fib_15 = next((fibonacci() for _ in range(15)))
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_15 == 0