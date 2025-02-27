import sympy

def is_left_right_truncatable(n):
    if '0' in str(n):
        return False
    while n > 0 and sympy.isprime(n):
        if not sympy.isprime(n):
            return False
        left, right = n
        left = int(str(left)[1:]) if left > 9 else 0
        right = right // 10 if right > 9 else 0
        if left == 0 and right == 0:
            break
        n = left if left != 0 else right
    return n > 1 and sympy.isprime(n)

def all_left_right_truncatable_prime(numbers):
    x = numbers[88]
    truncatable_primes = [n for n in range(2, x + 1) if is_left_right_truncatable(n)]
    return sorted(truncatable_primes, reverse=True)