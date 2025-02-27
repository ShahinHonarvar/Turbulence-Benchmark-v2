from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[0]

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:-i])):
                return False
        return True
    return [n for n in range(2, x + 1) if isprime(n) and is_truncatable_prime(n)][::-1]