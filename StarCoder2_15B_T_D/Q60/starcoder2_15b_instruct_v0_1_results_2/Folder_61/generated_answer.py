def all_left_right_truncatable_prime(x):
    """
    Finds all left-and-right-truncatable prime numbers less than or equal to x.
    """
    primes = sieve_of_eratosthenes(x)
    left_truncatable_primes = []
    for prime in primes:
        if is_left_truncatable_prime(prime):
            left_truncatable_primes.append(prime)
    right_truncatable_primes = []
    for prime in left_truncatable_primes:
        if is_right_truncatable_prime(prime):
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)

def is_left_truncatable_prime(prime):
    """
    Checks if a prime number is left-truncatable.
    """
    if prime < 10:
        return True
    digit = prime % 10
    if digit == 0:
        return False
    truncated_prime = prime // 10
    return is_prime(truncated_prime) and is_left_truncatable_prime(truncated_prime)

def is_right_truncatable_prime(prime):
    """
    Checks if a prime number is right-truncatable.
    """
    if prime < 10:
        return True
    digit = prime // 10
    if digit == 0:
        return False
    truncated_prime = prime % 10
    return is_prime(truncated_prime) and is_right_truncatable_prime(truncated_prime)

def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sieve_of_eratosthenes(n):
    """
    Finds all prime numbers less than or equal to n.
    """
    primes = [True for i in range(n + 1)]
    primes[0] = False
    primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]