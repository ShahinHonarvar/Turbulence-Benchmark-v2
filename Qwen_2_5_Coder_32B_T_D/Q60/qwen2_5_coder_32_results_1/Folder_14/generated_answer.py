import sympy

def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable_prime(n):
        s = str(n)
        for i in range(1, len(s)):
            if not (sympy.isprime(int(s[i:])) and sympy.isprime(int(s[:-i]))):
                return False
        return True
    x = numbers[78]
    result = [n for n in range(10, x + 1) if '0' not in str(n) and is_left_right_truncatable_prime(n) and sympy.isprime(n)]
    return sorted(result, reverse=True)