def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)

    def is_div_by_fib_110(decimal):
        fib_110 = fib(110)
        return decimal % fib_110 == 0
    decimal = binary_to_decimal(binary_str)
    return is_div_by_fib_110(decimal)