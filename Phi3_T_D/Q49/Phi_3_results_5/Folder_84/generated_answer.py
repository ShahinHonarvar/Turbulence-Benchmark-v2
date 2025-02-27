def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(binary_str):
        decimal = 0
        for digit in binary_str:
            decimal = decimal * 2 + int(digit)
        return decimal
    fib_196th = fib(196)
    decimal_number = binary_to_decimal(binary_str)
    return decimal_number % fib_196th == 0