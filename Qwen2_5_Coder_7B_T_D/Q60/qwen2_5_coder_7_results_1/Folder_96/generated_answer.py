from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[29]

    def is_left_right_truncatable_prime(n):
        s = str(n)
        for i in range(len(s)):
            if '0' in s[i:] or not isprime(int(s[i:])) or (not isprime(int(s[:len(s) - i]))):
                return False
        return True
    return sorted([n for n in range(2, x + 1) if isprime(n) and is_left_right_truncatable_prime(n)])