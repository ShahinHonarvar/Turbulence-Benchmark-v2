def if_decimal_is_divisible(binary_str):
    fibonacci_16 = 610 if len(binary_str) <= 11 else next((x for x in fibonacci_generator() if x >= 610))
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_16 == 0

def fibonacci_generator():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)