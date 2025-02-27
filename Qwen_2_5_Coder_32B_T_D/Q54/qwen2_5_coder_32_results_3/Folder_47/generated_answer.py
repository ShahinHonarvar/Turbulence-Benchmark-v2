from sympy import isprime

def all_right_truncatable_prime(numbers):

    def is_right_truncatable(n):
        while n > 0:
            if not isprime(n):
                return False
            n //= 10
        return True
    x = numbers[49]
    right_truncatable_primes = [n for n in range(2, x) if is_right_truncatable(n)]
    return sorted(right_truncatable_primes)