def if_decimal_is_divisible(binary_str):

    def fib_118():
        a, b = (0, 1)
        for i in range(117):
            a, b = (b, a + b)
        return a
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_118() == 0