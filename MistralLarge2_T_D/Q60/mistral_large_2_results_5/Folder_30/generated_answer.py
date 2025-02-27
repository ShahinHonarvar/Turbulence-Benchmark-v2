import sympy

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    num_str = str(n)
    left, right = (0, len(num_str) - 1)
    while left <= right:
        if not sympy.isprime(int(num_str[left:right + 1])):
            return False
        left += 1
        right -= 1
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[37]
    primes = [p for p in sympy.primerange(2, x + 1) if is_left_right_truncatable_prime(p)]
    return sorted(primes, reverse=True)