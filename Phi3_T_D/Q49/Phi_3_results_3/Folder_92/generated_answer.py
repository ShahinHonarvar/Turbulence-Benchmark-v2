def if_decimal_is_divisible(binary_str):

    def fibonacci_sequence(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)
    fib_num = fibonacci_sequence(6)
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_num == 0