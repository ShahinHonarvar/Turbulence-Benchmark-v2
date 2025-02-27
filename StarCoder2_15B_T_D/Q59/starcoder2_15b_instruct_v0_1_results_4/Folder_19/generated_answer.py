def all_left_truncatable_prime(nums):
    """
    Returns a list of all left-truncatable prime numbers less than the integer at index 67.
    """
    x = nums[67]
    primes = sieve_of_eratosthenes(x)
    left_truncatable_primes = []
    for prime in primes:
        is_left_truncatable = True
        temp = prime
        while temp > 0:
            if temp % 10 == 0:
                is_left_truncatable = False
                break
            temp //= 10
        if is_left_truncatable:
            left_truncatable_primes.append(prime)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes

def sieve_of_eratosthenes(n):
    """
    Returns a list of prime numbers less than or equal to n.
    """
    primes = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(2, n + 1) if primes[i]]