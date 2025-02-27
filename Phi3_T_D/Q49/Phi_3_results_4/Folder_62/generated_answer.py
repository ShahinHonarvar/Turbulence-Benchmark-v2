def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a

    def convert_binary_to_decimal(binary_str):
        decimal, i = (0, 0)
        while binary_str:
            decimal += int(binary_str[-1]) * 2 ** i
            binary_str = binary_str[:-1]
            i += 1
        return decimal
    fib_130 = fib(130)
    decimal = convert_binary_to_decimal(binary_str)
    return decimal % fib_130 == 0