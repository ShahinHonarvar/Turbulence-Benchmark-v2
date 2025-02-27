from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[86]

    def is_left_truncatable(n):
        s = str(n)
        while s:
            if not isprime(int(s)):
                return False
            s = s[1:]
        return True
    return sorted([n for n in range(2, x) if is_left_truncatable(n)], reverse=True)