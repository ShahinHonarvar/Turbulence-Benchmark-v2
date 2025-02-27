import sympy

def all_left_right_truncatable_prime(numbers):

    def is_lr_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s) - 1):
            if not (sympy.isprime(int(s[i:])) and sympy.isprime(int(s[:-i]))):
                return False
        return sympy.isprime(n)
    x = numbers[65]
    result = [n for n in range(11, x + 1) if is_lr_truncatable_prime(n)]
    return sorted(result, reverse=True)