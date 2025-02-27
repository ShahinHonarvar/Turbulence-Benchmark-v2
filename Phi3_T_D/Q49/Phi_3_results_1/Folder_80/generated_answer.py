def if_decimal_is_divisible(binary_str):
    fib_cache = {0: 0, 1: 1}

    def find_fibonacci(n):
        if n not in fib_cache:
            fib_cache[n] = find_fibonacci(n - 1) + find_fibonacci(n - 2)
        return fib_cache[n]

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)

    def is_divisible(decimal, divisor):
        return decimal % divisor == 0
    if len(binary_str) < 32:
        decimal_number = binary_to_decimal(binary_str)
        fib_179 = find_fibonacci(178)
        return is_divisible(decimal_number, fib_179)
    else:
        return False