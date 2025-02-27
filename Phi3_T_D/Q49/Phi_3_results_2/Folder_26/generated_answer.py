from math import sqrt

def if_decimal_is_divisible(binary_str):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def get_fibonacci_at_position(position):
        a, b = (0, 1)
        for _ in range(position - 1):
            a, b = (b, a + b)
        return a
    decimal_val = int(binary_str, 2)
    fibonacci_target = get_fibonacci_at_position(138)
    return decimal_val % fibonacci_target == 0