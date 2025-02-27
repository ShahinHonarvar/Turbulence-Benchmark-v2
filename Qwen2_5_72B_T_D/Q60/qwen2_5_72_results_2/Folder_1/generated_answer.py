import sympy

def all_left_right_truncatable_prime(numbers):
    x = numbers[20]

    def is_left_right_truncatable_prime(n):
        if not sympy.isprime(n) or '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not sympy.isprime(int(str(n)[i:])) or not sympy.isprime(int(str(n)[:-i])):
                return False
        return True
    primes = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    return sorted(primes, reverse=True)