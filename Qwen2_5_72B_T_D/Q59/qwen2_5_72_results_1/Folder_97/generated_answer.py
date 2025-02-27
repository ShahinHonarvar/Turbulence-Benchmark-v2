from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[645]

    def is_left_truncatable_prime(n):
        s = str(n)
        for i in range(len(s)):
            if not isprime(int(s[i:])):
                return False
        return True
    result = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    return sorted(result)