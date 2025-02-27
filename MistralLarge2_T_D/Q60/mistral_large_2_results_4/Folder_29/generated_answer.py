from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[55]

    def is_left_right_truncatable_prime(n):
        if not isprime(n):
            return False
        s = str(n)
        if '0' in s:
            return False
        for _ in range(len(s) - 1):
            s = s[1:-1]
            if not isprime(int(s)):
                return False
        return isprime(int(s))
    return sorted((n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)), reverse=True)