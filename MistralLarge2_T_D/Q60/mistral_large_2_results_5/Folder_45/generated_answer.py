from sympy import isprime

def is_left_right_truncatable_prime(n):
    s = str(n)
    if '0' in s or not isprime(n):
        return False
    while len(s) > 2:
        s = s[1:-1]
        if not isprime(int(s)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[61]
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)])