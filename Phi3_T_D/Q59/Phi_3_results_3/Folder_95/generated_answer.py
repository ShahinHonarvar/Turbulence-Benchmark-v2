from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[77]
    left_truncatable_primes = []

    def is_left_truncatable(n):
        if not isprime(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True
    for prime in map(isprime, range(2, x)):
        if is_left_truncatable(prime):
            left_truncatable_primes.append(prime)
    return left_truncatable_primes