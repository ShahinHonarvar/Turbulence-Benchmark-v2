import sympy

def is_left_truncatable(n):
    while n > 0:
        if not sympy.isprime(n):
            return False
        n = n % 10 ** (len(str(n)) - 1)
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[70]
    return sorted([n for n in range(2, x) if is_left_truncatable(n)], reverse=True)