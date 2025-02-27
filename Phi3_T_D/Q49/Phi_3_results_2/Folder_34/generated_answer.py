from math import sqrt

def if_decimal_is_divisible(binary_str):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def nth_fibonacci(n):
        sqrt5 = sqrt(5)
        phi = (1 + sqrt5) / 2
        return round(phi ** n / sqrt5)
    decimal = int(binary_str, 2)
    fib_24 = nth_fibonacci(24)
    if fib_24 == 0 or decimal % fib_24 != 0:
        return False
    return True