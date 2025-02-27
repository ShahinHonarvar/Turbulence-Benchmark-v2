from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[38]
    if x <= 2:
        return []

    def is_left_truncatable(n, x):
        if not isprime(n) or '0' in str(n):
            return False
        while n > 0:
            n = n % 10 ** (len(str(n)) - 1)
            if not isprime(n):
                return False
        return True
    return sorted([i for i in range(2, x) if is_left_truncatable(i, x)], reverse=True)