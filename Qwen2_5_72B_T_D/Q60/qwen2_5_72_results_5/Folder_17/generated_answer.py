from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[36]

    def is_left_right_truncatable_prime(n):
        if not isprime(n) or '0' in str(n):
            return False
        s = str(n)
        while len(s) > 1:
            if not isprime(int(s)):
                return False
            s = s[1:-1]
        return True
    return [n for n in range(x, 0, -1) if is_left_right_truncatable_prime(n)]