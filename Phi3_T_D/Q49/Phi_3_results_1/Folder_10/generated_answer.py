def if_decimal_is_divisible(binary_str):

    def fibonacci():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)
    decimal = int(binary_str, 2)
    for index, fib_num in enumerate(fibonacci(), 1):
        if index == 88:
            return decimal % fib_num == 0