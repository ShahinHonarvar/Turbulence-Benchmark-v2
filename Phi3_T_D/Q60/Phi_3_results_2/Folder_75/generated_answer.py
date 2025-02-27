from sympy import isprime

def is_left_right_truncatable_prime(n, primes):
    while n > 0:
        if not isprime(n):
            return False
        n = n % 10 ** (len(str(n)) - 1)
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[41]
    primes = set(range(2, x + 1))
    for i in range(2, int(x ** 0.5) + 1):
        if i in primes:
            primes -= set(range(i * 2, x + 1, i))
    primes = sorted(primes)
    return [p for p in primes if is_left_right_truncatable_prime(p, primes)]