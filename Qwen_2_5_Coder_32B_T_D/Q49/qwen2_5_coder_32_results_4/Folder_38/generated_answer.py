def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    f_78 = fibonacci(77)
    decimal_value = int(binary_str, 2)
    return decimal_value % f_78 == 0