def if_decimal_is_divisible(binary_str):

    def is_divisible_by_fibonacci(decimal_value, fib_index):
        a, b = (0, 1)
        for _ in range(fib_index):
            a, b = (b, a + b)
        return decimal_value % a == 0
    decimal_value = int(binary_str, 2)
    return is_divisible_by_fibonacci(decimal_value, 5)