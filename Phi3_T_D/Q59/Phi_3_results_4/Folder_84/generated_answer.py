from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[630]
    primes = [i for i in range(2, x) if isprime(i)]
    left_truncatable_primes = []

    def is_left_truncatable(p):
        s = str(p)
        while s:
            if not isprime(int(s)):
                return False
            s = s[1:]
        return True
    for p in primes:
        if is_left_truncatable(p):
            left_truncatable_primes.append(p)
    return sorted(left_truncatable_primes, reverse=True)