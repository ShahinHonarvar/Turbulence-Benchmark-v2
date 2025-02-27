import sympy

def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not sympy.isprime(int(str(n)[i:])) or not sympy.isprime(int(str(n)[:-i])):
                return False
        return True
    x = numbers[758]
    primes = list(sympy.primerange(2, x + 1))
    truncatable_primes = [p for p in primes if is_left_right_truncatable_prime(p)]
    return truncatable_primes