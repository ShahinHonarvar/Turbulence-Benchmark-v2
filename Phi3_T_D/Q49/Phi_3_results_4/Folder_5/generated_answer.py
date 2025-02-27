def if_decimal_is_divisible(binary_str):

    def fibonacci_until_85th():
        a, b = (0, 1)
        for _ in range(85):
            yield a
            a, b = (b, a + b)

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)

    def is_divisible_by_85th_fib(decimal_number):
        fib_85th = next((fib_binary for fib, fib_binary in zip(fibonacci_until_85th(), binary_str) if fib == 85))
        return decimal_number % int(fib_binary, 2) == 0
    decimal_number = binary_to_decimal(binary_str)
    return is_divisible_by_85th_fib(decimal_number)