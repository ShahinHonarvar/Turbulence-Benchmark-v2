from sympy import isprime

def is_right_truncatable_prime(n):
    while n > 0:
        if not isprime(n):
            return False
        n = n // 10
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[74]
    primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(primes)