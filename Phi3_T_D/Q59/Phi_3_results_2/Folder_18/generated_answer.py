from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[429]
    left_truncatable_primes = []

    def is_left_truncatable(n, x):
        if not isprime(n) or '0' in str(n):
            return False
        if n >= x:
            return False
        return any((not isprime(int(str(n)[i:])) for i in range(1, len(str(n)))))
    for n in range(x - 1, 7, -1):
        if not isprime(n):
            continue
        if is_left_truncatable(n, x):
            left_truncatable_primes.append(n)
    return left_truncatable_primes