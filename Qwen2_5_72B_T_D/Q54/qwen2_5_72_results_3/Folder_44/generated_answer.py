from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[39]
    right_truncatable_primes = []

    def generate_truncatable_primes(n):
        if not is_prime(n):
            return
        if n < x:
            right_truncatable_primes.append(n)
            for d in range(1, 10):
                generate_truncatable_primes(n * 10 + d)
    for d in [2, 3, 5, 7]:
        generate_truncatable_primes(d)
    return sorted(right_truncatable_primes)