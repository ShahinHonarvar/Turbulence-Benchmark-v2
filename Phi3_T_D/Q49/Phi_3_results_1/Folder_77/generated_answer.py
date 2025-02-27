def fibonacci_at(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def from_binary_string(binary_str):
    return int(binary_str, 2)

def if_decimal_is_divisible(binary_str):
    decimal_num = from_binary_string(binary_str)
    fib_num = fibonacci_at(110)
    return decimal_num % fib_num == 0