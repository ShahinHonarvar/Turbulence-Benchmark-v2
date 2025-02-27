from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        while len(s) > 1:
            if not isprime(int(s[1:-1])):
                return False
            s = s[1:-1]
        return isprime(int(s))
    x = numbers[945]
    return sorted([n for n in range(2, x + 1) if isprime(n) and is_truncatable(n)], reverse=True)