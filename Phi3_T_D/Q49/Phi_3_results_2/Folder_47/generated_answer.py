def if_decimal_is_divisible(binary_str):
    fibonacci_a, fibonacci_b = (0, 1)
    for _ in range(94):
        fibonacci_a, fibonacci_b = (fibonacci_b, fibonacci_a + fibonacci_b)
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_a == 0