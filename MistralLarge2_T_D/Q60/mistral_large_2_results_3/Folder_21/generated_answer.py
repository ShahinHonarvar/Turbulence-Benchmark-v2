from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[175]

    def is_left_right_truncatable(n):
        if n < 10:
            return isprime(n)
        s = str(n)
        if '0' in s:
            return False
        while len(s) > 1:
            if not isprime(int(s)):
                return False
            s = s[1:-1]
        return isprime(int(s))
    return sorted([i for i in range(2, x + 1) if is_left_right_truncatable(i)])