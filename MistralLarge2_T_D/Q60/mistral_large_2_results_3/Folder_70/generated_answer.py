from sympy import isprime

def is_left_right_truncatable_prime(n):
    if not isprime(n) or '0' in str(n):
        return False
    left, right = (str(n), str(n))
    while len(left) > 1 and len(right) > 1:
        left = left[1:]
        right = right[:-1]
        if not (isprime(int(left)) and isprime(int(right))):
            return False
    return isprime(int(left)) and isprime(int(right))

def all_left_right_truncatable_prime(numbers):
    x = numbers[433]
    truncatable_primes = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)