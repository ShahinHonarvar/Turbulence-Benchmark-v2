def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    fibonacci_number = fibonacci(59)
    decimal_integer = int(binary_representation, 2)
    return decimal_integer % fibonacci_number == 0