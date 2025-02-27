def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    nth_fib_number = fibonacci(95)
    decimal_number = binary_to_decimal(binary_str)
    return decimal_number % nth_fib_number == 0