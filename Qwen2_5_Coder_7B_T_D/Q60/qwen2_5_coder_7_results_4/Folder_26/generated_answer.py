from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[81]

    def is_left_right_truncatable(n):
        s = str(n)
        for i in range(len(s)):
            if '0' in str(int(s[i:])):
                return False
            if not isprime(int(s[i:])):
                return False
            if not isprime(int(s[:len(s) - i])):
                return False
        return True
    truncatable_primes = [n for n in range(2, x + 1) if isprime(n) and is_left_right_truncatable(n)]
    return sorted(truncatable_primes, reverse=True)