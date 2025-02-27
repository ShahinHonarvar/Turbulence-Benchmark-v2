from sympy import isprime

def left_truncatable_prime(n):
    while n > 0:
        if not isprime(n) or '0' in str(n):
            return False
        n = int(str(n)[1:])
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[645]
    return sorted([n for n in range(2, x) if left_truncatable_prime(n)])