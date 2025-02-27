def if_decimal_is_divisible(binary_str):

    def power(x, y):
        if y == 0:
            return 1
        while y > 1:
            x = x * x
            y -= 1
        return x

    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    decimal = 0
    for i in range(len(binary_str)):
        decimal += int(binary_str[i]) * power(2, len(binary_str) - i - 1)
    fib_154 = fib(154)
    return decimal % fib_154 == 0