def if_decimal_is_divisible(binary_str):

    def next_fibonacci(a, b):
        return (b, a + b)

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    if not binary_str or not binary_str.isdigit():
        return False
    fibonacci_limit = 105
    a, b = (0, 1)
    for _ in range(fibonacci_limit):
        a, b = next_fibonacci(a, b)
    decimal_value = binary_to_decimal(binary_str)
    return decimal_value % a == 0