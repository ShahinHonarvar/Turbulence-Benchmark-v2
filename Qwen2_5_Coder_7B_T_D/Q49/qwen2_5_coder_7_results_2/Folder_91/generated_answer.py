def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n - 1]
    decimal_number = int(binary_str, 2)
    sixth_fibonacci = fibonacci(6)
    return decimal_number % sixth_fibonacci == 0