from sympy import isprime

def all_left_right_truncatable_prime(tup):

    def is_left_right_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        while len(s) > 1:
            if not isprime(int(s)):
                return False
            s = s[1:-1]
        return True
    x = tup[22]
    truncatable_primes = [n for n in range(2, x + 1) if is_left_right_truncatable(n)]
    return sorted(truncatable_primes, reverse=True)