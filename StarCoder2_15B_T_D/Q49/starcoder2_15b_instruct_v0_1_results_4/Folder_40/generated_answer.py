def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    fibonacci_numbers = [fibonacci(i) for i in range(100)]
    decimal_integer = int(binary_representation, 2)
    return decimal_integer % fibonacci_numbers[3] == 0