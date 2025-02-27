def all_left_truncatable_prime(nums):
    x = nums[792]
    return sorted([p for p in left_truncatable_primes(x) if p < x])

def left_truncatable_primes(n):
    primes = sieve_of_eratosthenes(n)
    return [p for p in primes if is_left_truncatable_prime(p)]

def is_left_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    if not is_prime(n):
        return False
    return is_left_truncatable_prime(int(str(n)[1:]))

def sieve_of_eratosthenes(n):
    is_prime = [True] * n
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n, p):
                is_prime[i] = False
    return [p for p in range(2, n) if is_prime[p]]

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True