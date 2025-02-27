from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[975]

    def is_left_truncatable_prime(n):
        for i in range(1, len(str(n)) + 1):
            if not isprime(int(str(n)[:i])):
                return False
        return True
    primes = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    return sorted(primes, reverse=True)