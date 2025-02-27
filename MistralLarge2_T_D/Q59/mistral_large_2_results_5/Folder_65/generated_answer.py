from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[32]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []

    def is_left_truncatable(n):
        while n:
            if not isprime(n) or '0' in str(n):
                return False
            n = int(str(n)[1:])
        return True
    for i in range(5, x):
        if is_left_truncatable(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)