from math import sqrt

def if_decimal_is_divisible(binary_representation):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    nth_fib = 0
    a, b = (0, 1)
    count = 0
    while count < 80:
        c = a + b
        if is_prime(c):
            nth_fib = c
            count += 1
        a, b = (b, c)
    decimal_value = int(binary_representation, 2)
    return decimal_value % nth_fib == 0