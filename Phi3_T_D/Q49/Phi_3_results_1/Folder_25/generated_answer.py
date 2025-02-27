def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    fib_number = fibonacci(19)
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_number == 0