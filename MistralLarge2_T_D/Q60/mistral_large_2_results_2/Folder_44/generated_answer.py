import sympy

def all_left_right_truncatable_prime(tup):
    x = tup[39]
    primes = [p for p in sympy.primerange(2, x + 1) if '0' not in str(p)]

    def is_left_right_truncatable(n):
        s = str(n)
        while len(s) > 1:
            if not sympy.isprime(int(s[1:-1])):
                return False
            s = s[1:-1]
        return True
    return sorted([p for p in primes if is_left_right_truncatable(p)])