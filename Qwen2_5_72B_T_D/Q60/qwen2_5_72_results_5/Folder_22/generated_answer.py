from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        s = str(n)
        while s:
            if not isprime(int(s)):
                return False
            s = s[1:-1]
        return True
    x = numbers[85]
    return [n for n in range(2, x + 1) if is_truncatable_prime(n)]