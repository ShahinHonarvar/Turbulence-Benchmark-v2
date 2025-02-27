from itertools import takewhile, count
    from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[54]

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not isprime(int(str_n[i:])) or not isprime(int(str_n[:-i])):
                return False
        return isprime(n)
    primes = (i for i in count(2) if isprime(i))
    truncatable_primes = [p for p in takewhile(lambda p: p <= x, primes) if is_truncatable_prime(p)]
    return truncatable_primes