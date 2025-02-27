def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fibonacci_180 = calculate_fibonacci(180)
    return decimal_value % fibonacci_180 == 0

def calculate_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)