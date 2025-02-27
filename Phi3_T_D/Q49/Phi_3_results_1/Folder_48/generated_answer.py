def if_decimal_is_divisible(binary_str):

    def fib_number(index):
        a, b = (0, 1)
        for _ in range(index - 1):
            a, b = (b, a + b)
        return a
    fib198 = fib_number(198)
    decimal_num = int(binary_str, 2)
    return decimal_num % fib198 == 0