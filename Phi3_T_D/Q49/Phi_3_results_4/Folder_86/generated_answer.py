from math import sqrt

def if_decimal_is_divisible(binary_str):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def tau(n, p):
        result, exponent = (1, 0)
        while n % p == 0:
            n //= p
            exponent += 1
        return (result, exponent)

    def prime_factorize(n):
        factors, max_factor = ({}, 2)
        while n > 1 and max_factor <= sqrt(n):
            if n % max_factor == 0:
                exponent = 0
                while n % max_factor == 0:
                    n //= max_factor
                    exponent += 1
                factors[max_factor] = exponent
            max_factor += 1
        if n > 1:
            factors[n] = 1
        return factors

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, (a + b) % 10 ** 9)
        return a
    dec_num = int(binary_str, 2)
    target_fib = 135
    target_val = fibonacci(target_fib)
    if dec_num % target_val == 0:
        return True
    else:
        return False