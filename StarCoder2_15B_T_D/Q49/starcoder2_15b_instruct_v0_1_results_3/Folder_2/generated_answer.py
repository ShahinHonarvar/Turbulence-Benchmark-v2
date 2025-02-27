def if_decimal_is_divisible(binary_string):
    """
    Check if a decimal integer represented in binary is divisible by the 125th Fibonacci number.
    """
    decimal_integer = int(binary_string, base=2)

    def calculate_fibonacci(n):
        if n <= 1:
            return n
        return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)
    fibonacci_125 = calculate_fibonacci(125)
    return decimal_integer % fibonacci_125 == 0