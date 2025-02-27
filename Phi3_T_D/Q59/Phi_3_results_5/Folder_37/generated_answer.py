from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[35]

    def is_left_truncatable(n, max_val):
        while n > 0:
            if not isprime(n):
                return False
            n = n % 10 ** (len(str(n)) - 1)
        return True
    left_truncatable_primes = sorted(filter(lambda n: is_left_truncatable(n, x) and n < x, range(2, x)), reverse=True)
    return left_truncatable_primes