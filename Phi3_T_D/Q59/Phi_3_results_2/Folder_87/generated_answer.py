from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[39]
    truncation_primes = []

    def all_left_primes(num, list=[]):
        if num < x:
            if isprime(num) and all(map(lambda y: isprime(y), map(str.lstrip, map(str, range(num, x, -1))))):
                truncation_primes.extend(map(int, map(str.lstrip, map(str, range(num, x, -1)))))
                return True
            return False
        return False
    for num in range(2, x, -1):
        all_left_primes(num)
    truncation_primes.sort(reverse=True)
    return truncation_primes