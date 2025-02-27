def if_decimal_is_divisible(binary_string):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    decimal_number = binary_to_decimal(binary_string)
    fibonacci_number = fib(75)
    return decimal_number % fibonacci_number == 0