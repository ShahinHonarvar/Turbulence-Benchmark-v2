import sympy

def all_right_truncatable_prime(numbers):
    x = numbers[94]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)

def is_right_truncatable_prime(num):
    while num > 0:
        if not sympy.isprime(num):
            return False
        num //= 10
    return True