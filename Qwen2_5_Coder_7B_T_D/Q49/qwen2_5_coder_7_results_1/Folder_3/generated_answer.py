def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib = [0] * (n + 1)
        fib[1] = 1
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib_35 = fibonacci(35)[-1]
    decimal = binary_to_decimal(binary_str)
    return decimal % fib_35 == 0