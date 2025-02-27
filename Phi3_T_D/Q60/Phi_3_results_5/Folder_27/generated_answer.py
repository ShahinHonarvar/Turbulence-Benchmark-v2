from sympy import isprime

def all_left_right_truncatable_prime(args):

    def _is_truncatable_prime(n, d):
        str_n = str(n)
        if len(str_n) < d or not isprime(n):
            return False
        for i in range(d, len(str_n) + 1):
            if not isprime(int(str_n[i:])):
                return False
        for i in range(0, d):
            if not isprime(int(str_n[:i + 1])):
                return False
        return True
    x = args[79] if len(args) > 79 else None
    if x is None:
        return []
    return sorted([i for i in range(23, x + 1) if _is_truncatable_prime(i, 2)], reverse=True)