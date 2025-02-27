from sympy import isprime

def all_left_right_truncatable_prime(t):

    def is_lr_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:-i])):
                return False
        return True
    x = t[20]
    result = [n for n in range(11, x + 1) if is_lr_truncatable(n)]
    return sorted(result, reverse=True)