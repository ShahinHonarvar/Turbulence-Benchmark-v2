def if_decimal_is_divisible(binary_string):

    def decimal_from_binary(binary_string):
        return int(binary_string, 2)

    def fib(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    number = decimal_from_binary(binary_string)
    fib_number = fib(118)
    return number % fib_number == 0