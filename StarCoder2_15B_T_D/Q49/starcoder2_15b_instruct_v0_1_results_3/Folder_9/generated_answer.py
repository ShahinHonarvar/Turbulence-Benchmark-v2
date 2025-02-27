def if_decimal_is_divisible(binary_representation):
    decimal_integer = 0
    for i, bit in enumerate(binary_representation):
        decimal_integer += int(bit) * 2 ** (len(binary_representation) - i - 1)

    def calculate_fibonacci(n):
        if n <= 1:
            return n
        return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)
    fibonacci_number = calculate_fibonacci(68)
    return decimal_integer % fibonacci_number == 0